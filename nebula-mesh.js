;(function () {
  'use strict';
  /* ═══════════════════════════════════════════════════════════════
   *  NEBULA-MESH  ·  Interactive Particle Background  v1.0
   *  ─────────────────────────────────────────────────────────────
   *  Hybrid: Galaxy Nebula  ×  FEM Structural Analysis Mesh
   *  Vanilla JS · Canvas 2D API · requestAnimationFrame · 60 fps
   *  © 2026 Luis Miguel Cruz Efus — Portafolio Profesional
   * ═══════════════════════════════════════════════════════════════ */

  const canvas = document.getElementById('nebula-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const DPR = Math.min(window.devicePixelRatio || 1, 2);

  /* ── Constants ─────────────────────────────────────────────── */
  const TAU       = Math.PI * 2;
  const CONN_DIST = 150;
  const CONN_SQ   = CONN_DIST * CONN_DIST;
  const CURSOR_R  = 180;
  const CURSOR_SQ = CURSOR_R * CURSOR_R;
  const SPRING    = 0.025;
  const DAMP      = 0.92;

  /* ── State ─────────────────────────────────────────────────── */
  let W, H, cx, cy, t = 0, animId = null;
  let nebulae = [], stars = [], nodes = [];
  let shoots  = [], nextShoot = 0;
  let pulses  = [];
  let mouse   = { x: -1e4, y: -1e4, on: false };
  let scrT = 0, scrS = 0;

  /* ── Reduced-motion preference ─────────────────────────────── */
  const rmq = window.matchMedia('(prefers-reduced-motion: reduce)');
  let reduced = rmq.matches;
  rmq.addEventListener('change', function (e) {
    reduced = e.matches;
    if (reduced) { cancelAnimationFrame(animId); renderStatic(); }
    else animate();
  });

  /* ── Helpers ───────────────────────────────────────────────── */
  var rand = function (a, b) { return Math.random() * (b - a) + a; };

  /* ══════════════════════════════════════════════════════════════
   *  FACTORIES — create particle layers
   * ══════════════════════════════════════════════════════════════ */

  /* ── Nebula gas clouds ─────────────────────────────────────── */
  function makeNebulae() {
    var pal = [
      [270, 55, 18], [285, 45, 25], [310, 48, 22],
      [240, 50, 20], [280, 60, 35], [195, 70, 30], [330, 40, 25]
    ];
    var m = Math.min(W, H);
    nebulae = [];
    for (var i = 0; i < 7; i++) {
      var c = pal[i];
      nebulae.push({
        ocx: cx + rand(-W * 0.22, W * 0.22),
        ocy: cy + rand(-H * 0.18, H * 0.18),
        or:  rand(m * 0.04, m * 0.22),
        a:   rand(0, TAU),
        av:  rand(5e-5, 2.2e-4) * (Math.random() > 0.5 ? 1 : -1),
        br:  rand(m * 0.28, m * 0.65),
        ph:  rand(0, TAU),
        bs:  rand(2e-4, 5e-4),
        ba:  rand(0.05, 0.12),
        al:  rand(0.03, 0.09),
        h: c[0], s: c[1], l: c[2],
        dp:  rand(0.02, 0.07)
      });
    }
  }

  /* ── Star field ────────────────────────────────────────────── */
  function makeStars() {
    var n = W < 768 ? 160 : 300;
    stars = [];
    for (var i = 0; i < n; i++) {
      var cyan = Math.random() < 0.06;
      stars.push({
        x: rand(0, W), y: rand(0, H),
        r: rand(0.3, 1.4),
        ba: rand(0.12, 0.45),
        ts: rand(0.0008, 0.0035),
        tp: rand(0, TAU),
        h: cyan ? rand(185, 200) : rand(210, 250),
        s: cyan ? 100 : rand(10, 35),
        l: cyan ? 72  : rand(80, 95),
        dp: rand(0.01, 0.04)
      });
    }
  }

  /* ── FEM mesh nodes ────────────────────────────────────────── */
  function makeNodes() {
    var count = W < 768 ? 55 : 95;
    var asp  = W / H;
    var cols = Math.ceil(Math.sqrt(count * asp));
    var rows = Math.ceil(count / cols);
    var cw   = W / cols, ch = H / rows;
    var pal  = [[275,50,65],[260,40,60],[290,45,60],[195,80,65],[240,50,65]];

    nodes = [];
    var idx = 0;
    for (var r = 0; r < rows && idx < count; r++) {
      for (var c = 0; c < cols && idx < count; c++, idx++) {
        var bx = (c + 0.5) * cw + rand(-cw * 0.35, cw * 0.35);
        var by = (r + 0.5) * ch + rand(-ch * 0.35, ch * 0.35);
        var dx = bx - cx, dy = by - cy;
        var cl = pal[idx % pal.length];
        var sr = Math.random();
        nodes.push({
          bx: bx, by: by, x: bx, y: by, vx: 0, vy: 0,
          r:  rand(1.4, 2.8),
          oR: Math.sqrt(dx * dx + dy * dy),
          oA: Math.atan2(dy, dx),
          oS: rand(6e-5, 1.6e-4) * (Math.random() > 0.5 ? 1 : -1),
          h: cl[0], s: cl[1], l: cl[2],
          al: rand(0.18, 0.38),
          gs: rand(5, 10),
          pp: rand(0, TAU),
          ps: rand(0.001, 0.003),
          sh: sr < 0.72 ? 0 : sr < 0.88 ? 1 : 2   // 0=circle  1=cross  2=diamond
        });
      }
    }
  }

  /* ══════════════════════════════════════════════════════════════
   *  UPDATE — physics & simulation step
   * ══════════════════════════════════════════════════════════════ */

  function update() {
    t++;
    scrS += (scrT - scrS) * 0.08;

    /* Nebula orbital drift */
    for (var i = 0; i < nebulae.length; i++) nebulae[i].a += nebulae[i].av;

    /* Mesh node dynamics */
    for (var i = 0; i < nodes.length; i++) {
      var nd = nodes[i];

      // Differential spiral orbit
      nd.oA += nd.oS;
      nd.bx = cx + nd.oR * Math.cos(nd.oA);
      nd.by = cy + nd.oR * Math.sin(nd.oA);

      // Cursor elastic repulsion (carga puntual)
      if (mouse.on) {
        var dx = nd.x - mouse.x, dy = nd.y - mouse.y;
        var dSq = dx * dx + dy * dy;
        if (dSq < CURSOR_SQ && dSq > 1) {
          var d = Math.sqrt(dSq);
          var f = (1 - d / CURSOR_R) * 0.8;
          nd.vx += (dx / d) * f;
          nd.vy += (dy / d) * f;
        }
      }

      // Spring-back to orbital base position
      nd.vx += (nd.bx - nd.x) * SPRING;
      nd.vy += (nd.by - nd.y) * SPRING;
      nd.vx *= DAMP;
      nd.vy *= DAMP;
      nd.x  += nd.vx;
      nd.y  += nd.vy;
    }

    /* Shooting stars */
    var now = performance.now();
    if (now > nextShoot) { spawnShoot(); nextShoot = now + rand(4000, 8000); }
    for (var i = shoots.length - 1; i >= 0; i--) {
      var s = shoots[i];
      s.x += s.vx; s.y += s.vy;
      s.trail.push({ x: s.x, y: s.y });
      if (s.trail.length > 8) s.trail.shift();
      s.life -= 0.012;
      if (s.life <= 0 || s.x < -60 || s.x > W + 60 || s.y < -60 || s.y > H + 60)
        shoots.splice(i, 1);
    }

    /* Connection stress pulses */
    if (Math.random() < 0.004) spawnPulse();
    for (var i = pulses.length - 1; i >= 0; i--) {
      pulses[i].p += 0.018;
      if (pulses[i].p > 1) pulses.splice(i, 1);
    }
  }

  function spawnShoot() {
    var a  = rand(2.35, 2.85);          // ~135°–163° in canvas coords
    var sp = rand(9, 16);
    var x0 = rand(W * 0.25, W + 40);
    var y0 = rand(-40, H * 0.3);
    shoots.push({
      x: x0, y: y0,
      vx: Math.cos(a) * sp,
      vy: Math.sin(a) * sp,
      trail: [{ x: x0, y: y0 }],
      life: 1
    });
  }

  function spawnPulse() {
    if (nodes.length < 2) return;
    var a = (Math.random() * nodes.length) | 0;
    for (var j = 0; j < nodes.length; j++) {
      if (j === a) continue;
      var dx = nodes[a].x - nodes[j].x, dy = nodes[a].y - nodes[j].y;
      if (dx * dx + dy * dy < CONN_SQ) {
        pulses.push({ a: a, b: j, p: 0 });
        return;
      }
    }
  }

  /* ══════════════════════════════════════════════════════════════
   *  RENDER — draw every layer bottom-to-top
   * ══════════════════════════════════════════════════════════════ */

  function render() {
    ctx.clearRect(0, 0, W, H);
    drawNebulae();
    drawVignette();
    drawStars();
    drawConns();
    drawNodes();
    drawHalo();
    drawShoots();
  }

  /* ── Layer 1: Nebula gas clouds (screen blend) ─────────────── */
  function drawNebulae() {
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    for (var i = 0; i < nebulae.length; i++) {
      var n = nebulae[i];
      var x = n.ocx + n.or * Math.cos(n.a);
      var y = n.ocy + n.or * Math.sin(n.a) - scrS * n.dp;
      var r = n.br * (1 + n.ba * Math.sin(t * n.bs + n.ph));
      var g = ctx.createRadialGradient(x, y, 0, x, y, r);
      g.addColorStop(0,   'hsla(' + n.h + ',' + n.s + '%,' + n.l + '%,' + n.al + ')');
      g.addColorStop(0.4, 'hsla(' + n.h + ',' + (n.s * .8 | 0) + '%,' + (n.l * .7 | 0) + '%,' + (n.al * .5) + ')');
      g.addColorStop(1,   'hsla(0,0%,0%,0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(x, y, r, 0, TAU);
      ctx.fill();
    }
    ctx.restore();
  }

  /* ── Vignette (depth framing) ──────────────────────────────── */
  function drawVignette() {
    var r = Math.max(W, H) * 0.75;
    var g = ctx.createRadialGradient(cx, cy, r * 0.3, cx, cy, r);
    g.addColorStop(0, 'transparent');
    g.addColorStop(1, 'rgba(21,23,28,0.45)');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);
  }

  /* ── Layer 2: Star field (twinkling) ───────────────────────── */
  function drawStars() {
    for (var i = 0, n = stars.length; i < n; i++) {
      var s  = stars[i];
      var tw = 0.5 + 0.5 * Math.sin(t * s.ts + s.tp);
      ctx.fillStyle = 'hsla(' + s.h + ',' + s.s + '%,' + s.l + '%,' + (s.ba * tw) + ')';
      ctx.beginPath();
      ctx.arc(s.x, s.y - scrS * s.dp, s.r, 0, TAU);
      ctx.fill();
    }
  }

  /* ── Layer 3: Mesh connections (FEM edges) ─────────────────── */
  function drawConns() {
    ctx.lineWidth = 0.5;
    for (var i = 0; i < nodes.length; i++) {
      var a = nodes[i];
      for (var j = i + 1; j < nodes.length; j++) {
        var b  = nodes[j];
        var dx = a.x - b.x, dy = a.y - b.y;
        var dSq = dx * dx + dy * dy;
        if (dSq >= CONN_SQ) continue;

        var d  = Math.sqrt(dSq);
        var al = (1 - d / CONN_DIST) * 0.12;

        // Amplify if an active stress pulse is on this edge
        for (var k = 0; k < pulses.length; k++) {
          var p = pulses[k];
          if ((p.a === i && p.b === j) || (p.a === j && p.b === i))
            al = Math.max(al, 0.35 * Math.sin(p.p * Math.PI));
        }

        ctx.strokeStyle = 'hsla(260,40%,55%,' + al + ')';
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.stroke();
      }
    }
  }

  /* ── Layer 4: Mesh nodes (FEM markers) ─────────────────────── */
  function drawNodes() {
    for (var i = 0, n = nodes.length; i < n; i++) {
      var nd  = nodes[i];
      var pul = 0.7 + 0.3 * Math.sin(t * nd.ps + nd.pp);
      var a   = nd.al * pul;
      var col = 'hsla(' + nd.h + ',' + nd.s + '%,' + nd.l + '%,' + a + ')';

      ctx.save();
      ctx.shadowBlur  = nd.gs;
      ctx.shadowColor = 'hsla(' + nd.h + ',' + nd.s + '%,' + nd.l + '%,' + (a * 0.5) + ')';

      if (nd.sh === 1) {
        /* Cross — constraint point */
        var s = nd.r * 1.5;
        ctx.strokeStyle = col;
        ctx.lineWidth   = 0.8;
        ctx.beginPath();
        ctx.moveTo(nd.x - s, nd.y); ctx.lineTo(nd.x + s, nd.y);
        ctx.moveTo(nd.x, nd.y - s); ctx.lineTo(nd.x, nd.y + s);
        ctx.stroke();
      } else if (nd.sh === 2) {
        /* Diamond — pinned support */
        var d = nd.r * 1.8;
        ctx.fillStyle = col;
        ctx.beginPath();
        ctx.moveTo(nd.x, nd.y - d);
        ctx.lineTo(nd.x + d * 0.55, nd.y);
        ctx.lineTo(nd.x, nd.y + d);
        ctx.lineTo(nd.x - d * 0.55, nd.y);
        ctx.closePath();
        ctx.fill();
      } else {
        /* Circle — standard node */
        ctx.fillStyle = col;
        ctx.beginPath();
        ctx.arc(nd.x, nd.y, nd.r, 0, TAU);
        ctx.fill();
      }

      ctx.restore();
    }
  }

  /* ── Cursor halo (interactive glow) ────────────────────────── */
  function drawHalo() {
    if (!mouse.on) return;
    var r = CURSOR_R * 0.7;
    var g = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, r);
    g.addColorStop(0,   'hsla(280,60%,50%,0.035)');
    g.addColorStop(0.5, 'hsla(260,50%,40%,0.015)');
    g.addColorStop(1,   'hsla(0,0%,0%,0)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(mouse.x, mouse.y, r, 0, TAU);
    ctx.fill();
  }

  /* ── Layer 5: Shooting stars (sporadic trails) ─────────────── */
  function drawShoots() {
    for (var i = 0; i < shoots.length; i++) {
      var s = shoots[i];
      if (s.trail.length < 2) continue;

      // Trail segments — opacity & width grow toward head
      for (var j = 1; j < s.trail.length; j++) {
        var pct = j / s.trail.length;
        ctx.strokeStyle = 'hsla(195,100%,80%,' + (pct * 0.6 * s.life) + ')';
        ctx.lineWidth   = pct * 2.2;
        ctx.beginPath();
        ctx.moveTo(s.trail[j - 1].x, s.trail[j - 1].y);
        ctx.lineTo(s.trail[j].x, s.trail[j].y);
        ctx.stroke();
      }

      // Bright head
      var hd = s.trail[s.trail.length - 1];
      ctx.fillStyle = 'hsla(195,100%,92%,' + (0.8 * s.life) + ')';
      ctx.beginPath();
      ctx.arc(hd.x, hd.y, 1.5, 0, TAU);
      ctx.fill();
    }
  }

  /* ══════════════════════════════════════════════════════════════
   *  STATIC RENDER — single frame for prefers-reduced-motion
   * ══════════════════════════════════════════════════════════════ */

  function renderStatic() {
    ctx.clearRect(0, 0, W, H);

    // Nebulae at initial orbital positions
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    for (var i = 0; i < nebulae.length; i++) {
      var n = nebulae[i];
      var x = n.ocx + n.or * Math.cos(n.a);
      var y = n.ocy + n.or * Math.sin(n.a);
      var g = ctx.createRadialGradient(x, y, 0, x, y, n.br);
      g.addColorStop(0,   'hsla(' + n.h + ',' + n.s + '%,' + n.l + '%,' + n.al + ')');
      g.addColorStop(0.4, 'hsla(' + n.h + ',' + (n.s * .8 | 0) + '%,' + (n.l * .7 | 0) + '%,' + (n.al * .5) + ')');
      g.addColorStop(1,   'hsla(0,0%,0%,0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(x, y, n.br, 0, TAU);
      ctx.fill();
    }
    ctx.restore();

    drawVignette();

    // Static stars (no twinkling)
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      ctx.fillStyle = 'hsla(' + s.h + ',' + s.s + '%,' + s.l + '%,' + (s.ba * 0.6) + ')';
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, TAU);
      ctx.fill();
    }

    // Static mesh connections
    ctx.lineWidth = 0.5;
    for (var i = 0; i < nodes.length; i++) {
      for (var j = i + 1; j < nodes.length; j++) {
        var dx = nodes[i].bx - nodes[j].bx, dy = nodes[i].by - nodes[j].by;
        var dSq = dx * dx + dy * dy;
        if (dSq < CONN_SQ) {
          var d = Math.sqrt(dSq);
          ctx.strokeStyle = 'hsla(260,40%,55%,' + ((1 - d / CONN_DIST) * 0.08) + ')';
          ctx.beginPath();
          ctx.moveTo(nodes[i].bx, nodes[i].by);
          ctx.lineTo(nodes[j].bx, nodes[j].by);
          ctx.stroke();
        }
      }
    }

    // Static mesh nodes
    for (var i = 0; i < nodes.length; i++) {
      var nd = nodes[i];
      ctx.fillStyle = 'hsla(' + nd.h + ',' + nd.s + '%,' + nd.l + '%,' + (nd.al * 0.5) + ')';
      ctx.beginPath();
      ctx.arc(nd.bx, nd.by, nd.r, 0, TAU);
      ctx.fill();
    }
  }

  /* ══════════════════════════════════════════════════════════════
   *  ANIMATION LOOP
   * ══════════════════════════════════════════════════════════════ */

  function animate() {
    update();
    render();
    animId = requestAnimationFrame(animate);
  }

  /* ══════════════════════════════════════════════════════════════
   *  EVENT HANDLERS
   * ══════════════════════════════════════════════════════════════ */

  window.addEventListener('resize', function () {
    W  = window.innerWidth;
    H  = window.innerHeight;
    cx = W * 0.5;
    cy = H * 0.5;
    canvas.width  = W * DPR;
    canvas.height = H * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    makeNebulae();
    makeStars();
    makeNodes();
    if (reduced) renderStatic();
  });

  window.addEventListener('scroll', function () {
    scrT = window.scrollY;
  }, { passive: true });

  document.addEventListener('mousemove', function (e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    mouse.on = true;
  });

  document.addEventListener('mouseleave', function () {
    mouse.on = false;
  });

  /* ══════════════════════════════════════════════════════════════
   *  BOOTSTRAP
   * ══════════════════════════════════════════════════════════════ */

  W  = window.innerWidth;
  H  = window.innerHeight;
  cx = W * 0.5;
  cy = H * 0.5;
  canvas.width  = W * DPR;
  canvas.height = H * DPR;
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);

  makeNebulae();
  makeStars();
  makeNodes();
  nextShoot = performance.now() + rand(2000, 5000);

  if (reduced) renderStatic();
  else animate();

})();
