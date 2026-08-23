# -*- coding: utf-8 -*-
"""Genera las 4 fichas de la seccion IA & Automatizacion del portafolio."""
import io, os

DEST = u"D:/LAPTOP_LMCE/PORTAFOLIO PROFESIONAL/ia"

CABECERA = u'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#15171c">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://luismiguelcruzefus.com/ia/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:site_name" content="LM Ingenier\u00eda e Innovaci\u00f3n \u2014 Luis Miguel Cruz Efus">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://luismiguelcruzefus.com/ia/{slug}.html">
<meta property="og:image" content="https://luismiguelcruzefus.com/imagenes/lm_ingenieria/{img}/00_caratula.png">
<meta property="og:locale" content="es_PE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://luismiguelcruzefus.com/imagenes/lm_ingenieria/{img}/00_caratula.png">

<link rel="icon" type="image/png" href="../imagenes/lm_ingenieria/marca_lm/logo.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<script src="https://cdn.tailwindcss.com"></script>

<style>
  :root{{
    --ink: oklch(0.16 0.012 250);
    --ink-deep: oklch(0.12 0.012 250);
    --surface: oklch(0.21 0.012 250);
    --line: oklch(0.35 0.012 250 / 0.6);
    --line-soft: oklch(0.35 0.012 250 / 0.25);
    --text: oklch(0.94 0.008 80);
    --text-dim: oklch(0.75 0.008 80);
    --muted: oklch(0.6 0.012 250);
    --accent: oklch(0.78 0.14 65);
    --accent-deep: oklch(0.68 0.14 65);
    --accent-soft: oklch(0.78 0.14 65 / 0.12);
    --accent-2: oklch(0.72 0.10 245);
    --accent-2-soft: oklch(0.72 0.10 245 / 0.12);
  }}
  *{{ -webkit-tap-highlight-color: transparent; }}
  html{{ scroll-behavior:smooth; }}
  body{{
    background: var(--ink); color: var(--text);
    font-family: 'Geist', system-ui, sans-serif;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
  }}
  .serif{{ font-family:'Instrument Serif', Georgia, serif; }}
  .mono{{ font-family:'JetBrains Mono', monospace; }}
  .display{{ font-family:'Instrument Serif', serif; font-weight:400; letter-spacing:-0.018em; line-height:0.95; }}
  .display em{{ font-style:italic; color: var(--accent); }}

  .blueprint-bg{{
    background-image:
      linear-gradient(oklch(0.35 0.012 250 / 0.18) 1px, transparent 1px),
      linear-gradient(90deg, oklch(0.35 0.012 250 / 0.18) 1px, transparent 1px);
    background-size: 56px 56px;
  }}

  .coord{{
    font-family:'JetBrains Mono', monospace;
    font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--muted); display:inline-flex; align-items:center; gap:0.5rem;
  }}
  .coord::before{{ content:""; width: 18px; height:1px; background: var(--accent); }}

  .chip{{
    display:inline-flex; padding: 4px 10px; border: 1px solid var(--line); border-radius: 99px;
    font-family:'JetBrains Mono', monospace; font-size: 0.66rem;
    color: var(--text-dim); letter-spacing: 0.06em; text-transform: uppercase;
  }}
  .chip.accent{{ border-color: var(--accent); color: var(--accent); }}

  .btn{{
    display:inline-flex; align-items:center; gap: 10px;
    padding: 12px 20px; border-radius: 4px; font-weight: 500; font-size: 0.9rem;
    transition: all .25s ease; border: 1px solid transparent; cursor: pointer;
  }}
  .btn-primary{{ background: var(--accent); color: var(--ink-deep); }}
  .btn-primary:hover{{ background: var(--accent-deep); }}
  .btn-ghost{{ background:transparent; color:var(--text); border-color: var(--line); }}
  .btn-ghost:hover{{ border-color: var(--accent); color: var(--accent); }}
  .btn-outline{{ background: transparent; color: var(--text); border-color: var(--accent); }}
  .btn-outline:hover{{ background: var(--accent-soft); color: var(--accent); }}

  [data-reveal]{{ opacity:0; transform:translateY(14px); transition: opacity .9s ease, transform .9s ease; }}
  [data-reveal].in{{ opacity:1; transform:translateY(0); }}

  .nav-bg{{ background: oklch(0.16 0.012 250 / 0.82); backdrop-filter: blur(14px); }}

  .feature{{ border-left: 1px solid var(--accent); padding: 4px 0 4px 18px; }}
  .feature h4{{ font-size: 0.95rem; font-weight: 500; margin-bottom: 4px; }}
  .feature p{{ font-size: 0.85rem; color: var(--text-dim); line-height: 1.5; }}

  .hero-cover{{
    background: oklch(0.10 0.012 250);
    border: 1px solid var(--line-soft);
    border-radius: 6px; overflow: hidden; position: relative;
    aspect-ratio: 9/16; max-width: 360px; margin: 0 auto;
    transition: border-color .25s ease, transform .25s ease;
  }}
  .hero-cover:hover{{ border-color: var(--accent); transform: translateY(-2px); }}
  .hero-cover img{{ width:100%; height:100%; object-fit: cover; display:block; }}
  .hero-cover::before, .hero-cover::after{{
    content:""; position:absolute; width: 14px; height: 14px;
    border: 1px solid var(--accent); z-index: 2;
  }}
  .hero-cover::before{{ top: 8px; left: 8px; border-right:none; border-bottom:none; }}
  .hero-cover::after{{ bottom: 8px; right: 8px; border-left:none; border-top:none; }}
  .hero-cover .fallback{{
    position:absolute; inset:0; display:flex; align-items:center; justify-content:center;
    text-align:center; padding: 0 24px;
  }}

  .atmosphere{{ position:fixed; inset:0; z-index:-1; overflow:hidden; pointer-events:none; }}
  .atmosphere .orb{{ position:absolute; border-radius:50%; filter:blur(120px); will-change:transform; }}
  .atmosphere .orb-amber{{ width:46vw; height:46vw; min-width:360px; min-height:360px; background:radial-gradient(circle, oklch(0.78 0.14 65 / 0.50), transparent 68%); top:-16vh; right:-8vw; opacity:.5; animation:driftA 30s ease-in-out infinite alternate; }}
  .atmosphere .orb-blue{{ width:52vw; height:52vw; min-width:400px; min-height:400px; background:radial-gradient(circle, oklch(0.62 0.12 245 / 0.55), transparent 68%); bottom:-22vh; left:-12vw; opacity:.55; animation:driftB 38s ease-in-out infinite alternate; }}
  .atmosphere .orb-cyan{{ width:34vw; height:34vw; min-width:280px; min-height:280px; background:radial-gradient(circle, oklch(0.72 0.10 215 / 0.42), transparent 70%); top:36%; left:40%; opacity:.4; animation:driftC 34s ease-in-out infinite alternate; }}
  @keyframes driftA{{ to{{ transform:translate(-7vw,8vh) scale(1.12); }} }}
  @keyframes driftB{{ to{{ transform:translate(8vw,-6vh) scale(1.15); }} }}
  @keyframes driftC{{ to{{ transform:translate(-6vw,-7vh) scale(1.2); }} }}
  @media (prefers-reduced-motion: reduce){{ .atmosphere .orb{{ animation:none; }} }}

  .spec-strip{{ display:grid; grid-template-columns:repeat(2,1fr); gap:1px; background:var(--line-soft); border:1px solid var(--line-soft); border-radius:6px; overflow:hidden; }}
  @media (min-width:768px){{ .spec-strip{{ grid-template-columns:repeat(4,1fr); }} }}
  .spec{{ background:oklch(0.16 0.012 250); padding:18px 20px; }}
  .spec .k{{ font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:0.16em; text-transform:uppercase; color:var(--muted); display:block; margin-bottom:8px; }}
  .spec .v{{ font-size:1rem; color:var(--text); line-height:1.3; }}
  .spec .sub{{ display:block; font-size:0.78rem; color:var(--muted); margin-top:3px; }}

  /* Listado tecnico (herramienta / que hace) */
  .tool-row{{
    display:grid; grid-template-columns: 1fr; gap: 4px;
    padding: 16px 0; border-bottom: 1px solid var(--line-soft);
  }}
  @media (min-width:768px){{ .tool-row{{ grid-template-columns: 260px 1fr; gap: 28px; align-items:baseline; }} }}
  .tool-row .n{{ font-family:'JetBrains Mono',monospace; font-size:0.72rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--accent); }}
  .tool-row .d{{ font-size:0.9rem; color:var(--text-dim); line-height:1.6; }}
</style>
</head>
<body>
<div class="atmosphere" aria-hidden="true"><span class="orb orb-amber"></span><span class="orb orb-blue"></span><span class="orb orb-cyan"></span></div>

<!-- NAV -->
<header class="fixed top-0 left-0 right-0 z-50 nav-bg border-b" style="border-color: var(--line-soft);">
  <div class="max-w-7xl mx-auto px-6 lg:px-10 h-16 flex items-center justify-between gap-4">
    <a href="../index.html#ia-automatizacion" class="flex items-center gap-3">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="color: var(--accent);"><path d="M13 7H1m0 0l5-5m-5 5l5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      <span class="mono text-xs uppercase tracking-[0.18em]" style="color: var(--text-dim);">Volver al portafolio</span>
    </a>
    <div class="hidden md:flex items-center gap-3">
      <span class="mono text-[0.62rem] uppercase tracking-[0.18em]" style="color: var(--muted);">{navlabel}</span>
    </div>
  </div>
</header>

<!-- HERO -->
<section class="relative pt-32 pb-16 lg:pt-40 lg:pb-24 overflow-hidden">
  <div class="absolute inset-0 blueprint-bg" style="opacity:0.4"></div>
  <div class="max-w-7xl mx-auto px-6 lg:px-10 relative">

    <div class="flex items-center justify-between mb-12">
      <div class="coord">{coord_izq}</div>
      <div class="coord hidden md:flex">{coord_der}</div>
    </div>

    <div class="grid lg:grid-cols-12 gap-12 items-start">
      <div class="lg:col-span-7">
        <div class="flex flex-wrap items-center gap-3 mb-8">
{chips}
        </div>
        <h1 class="display text-5xl md:text-6xl lg:text-7xl mb-10" data-reveal>
          {h1}
        </h1>
{parrafos}
        <div class="flex flex-wrap gap-4 mt-8" data-reveal>
{botones}
        </div>
      </div>

      <div class="lg:col-span-5" data-reveal>
        <div class="hero-cover">
          <img src="../imagenes/lm_ingenieria/{img}/00_caratula.png" alt="{alt}" onerror="this.style.display='none'; this.parentElement.insertAdjacentHTML('beforeend', '<div class=&quot;fallback&quot;><div><div class=&quot;mono text-[0.62rem] uppercase tracking-[0.18em] mb-3&quot; style=&quot;color: var(--accent);&quot;>{fb_kicker}</div><div class=&quot;serif text-3xl leading-tight&quot;>{fb_titulo}</div></div></div>');">
        </div>
        <p class="mono text-[0.66rem] uppercase tracking-[0.14em] mt-4 text-center" style="color: var(--muted);">{pie_caratula}</p>
      </div>
    </div>

    <div class="spec-strip mt-14" data-reveal>
{specs}
    </div>
  </div>
</section>

<!-- SECCION A -->
<section class="py-20 lg:py-28 border-t" style="border-color: var(--line-soft); background: oklch(0.12 0.012 250 / 0.66);">
  <div class="max-w-7xl mx-auto px-6 lg:px-10">

    <div class="flex items-baseline gap-5 mb-12">
      <span class="mono text-sm" style="color: var(--accent);">\u00a7 A</span>
      <h2 class="serif text-3xl lg:text-4xl">{titulo_a}</h2>
    </div>

    <div class="grid md:grid-cols-2 gap-x-12 gap-y-8">
{features}
    </div>
  </div>
</section>

<!-- SECCION B -->
<section class="py-20 lg:py-28 border-t" style="border-color: var(--line-soft);">
  <div class="max-w-7xl mx-auto px-6 lg:px-10">

    <div class="flex items-baseline gap-5 mb-10">
      <span class="mono text-sm" style="color: var(--accent);">\u00a7 B</span>
      <h2 class="serif text-3xl lg:text-4xl">{titulo_b}</h2>
    </div>

    <div class="mt-2">
{filas}
    </div>
  </div>
</section>

<!-- SECCION C -->
<section class="py-20 lg:py-28 border-t" style="border-color: var(--line-soft); background: oklch(0.12 0.012 250 / 0.66);">
  <div class="max-w-5xl mx-auto px-6 lg:px-10">
    <div class="coord mb-6">\u00a7 C / {kicker_c}</div>
    <h2 class="display text-4xl md:text-5xl mb-10" data-reveal>
      {titulo_c}
    </h2>
    <div class="space-y-6 text-lg leading-relaxed" style="color: var(--text-dim);" data-reveal>
{cierre}
    </div>
  </div>
</section>

<!-- CTA -->
<section class="py-24 lg:py-32 relative overflow-hidden">
  <div class="absolute inset-0 blueprint-bg" style="opacity:0.3"></div>
  <div class="max-w-5xl mx-auto px-6 lg:px-10 relative text-center">
    <div class="coord justify-center mb-8" style="display:inline-flex;">N.99 \u00b7 M\u00e1s desarrollo propio</div>
    <h2 class="display text-4xl md:text-5xl mb-10">
      Explora el resto del<br><em>ecosistema de automatizaci\u00f3n</em>.
    </h2>
    <div class="flex flex-wrap justify-center gap-4">
      <a href="../index.html#ia-automatizacion" class="btn btn-outline">
        Ver IA &amp; Automatizaci\u00f3n
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M1 7h12m0 0L8 2m5 5l-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      </a>
      <a href="../index.html#aplicaciones" class="btn btn-ghost">Ver aplicaciones publicadas</a>
      <a href="../index.html#contacto" class="btn btn-primary">
        Conversemos
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M1 7h12m0 0L8 2m5 5l-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      </a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="py-10 border-t" style="border-color: var(--line-soft); background: oklch(0.12 0.012 250 / 0.66);">
  <div class="max-w-7xl mx-auto px-6 lg:px-10 flex flex-wrap items-center justify-between gap-4">
    <a href="../index.html" class="flex items-center gap-3">
      <div class="text-sm font-medium">Luis Miguel Cruz Efus</div>
    </a>
    <div class="mono text-xs uppercase tracking-[0.14em]" style="color: var(--muted);">
      {footlabel}
    </div>
  </div>
</footer>

<script>
  const io = new IntersectionObserver((entries) => {{
    entries.forEach(e => {{
      if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }}
    }});
  }}, {{ threshold: 0.12, rootMargin: '0px 0px -40px 0px' }});
  document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));
</script>
</body>
</html>
'''


def chips(lista):
    out = []
    for i, c in enumerate(lista):
        cls = u'chip accent' if i == 0 else u'chip'
        out.append(u'          <span class="%s">%s</span>' % (cls, c))
    return u'\n'.join(out)


def parrafos(lista):
    out = []
    for i, p in enumerate(lista):
        size = u'text-lg' if i == 0 else u'text-base'
        out.append(u'        <p class="%s leading-relaxed max-w-2xl mb-6" style="color: var(--text-dim);" data-reveal>\n          %s\n        </p>' % (size, p))
    return u'\n'.join(out)


def specs(lista):
    out = []
    for s in lista:
        sub = u'<span class="sub">%s</span>' % s[2] if len(s) > 2 and s[2] else u''
        out.append(u'        <div class="spec"><span class="k">%s</span><span class="v">%s</span>%s</div>' % (s[0], s[1], sub))
    return u'\n'.join(out)


def features(lista):
    out = []
    for t, d in lista:
        out.append(u'      <div class="feature" data-reveal>\n        <h4>%s</h4>\n        <p>%s</p>\n      </div>' % (t, d))
    return u'\n'.join(out)


def filas(lista):
    out = []
    for n, d in lista:
        out.append(u'      <div class="tool-row" data-reveal>\n        <div class="n">%s</div>\n        <div class="d">%s</div>\n      </div>' % (n, d))
    return u'\n'.join(out)


def cierre(lista):
    return u'\n'.join(u'      <p>%s</p>' % p for p in lista)


def botones(lista):
    out = []
    for texto, href, estilo, externo in lista:
        tgt = u' target="_blank" rel="noopener"' if externo else u''
        out.append(u'          <a href="%s"%s class="btn %s">\n            %s\n            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M1 7h12m0 0L8 2m5 5l-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>\n          </a>' % (href, tgt, estilo, texto))
    return u'\n'.join(out)


PAGINAS = []

# ─────────────────────────────────────────────────────────────────────────
# 1. LMBIMTools
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'lmbimtools',
    img=u'lmbimtools',
    title=u'LMBIMTools \u2014 Add-In de acero de refuerzo para Autodesk Revit \u00b7 Luis Miguel Cruz Efus',
    desc=u'LMBIMTools: suite de nueve herramientas en C#/.NET para Autodesk Revit 2025, 2026 y 2027 que modela en 3D el acero de columnas, vigas, zapatas, muros y losas bajo la norma peruana E.060 y genera el despiece 2D acotado.',
    navlabel=u'IA.01 \u00b7 Complementos BIM',
    footlabel=u'IA.01 \u00b7 LMBIMTools',
    coord_izq=u'IA.01 / Complementos BIM',
    coord_der=u'Revit API \u00b7 .NET 8 y .NET 10 \u00b7 NTE E.060',
    chips=chips([u'Desarrollo propio', u'Revit 2025 \u00b7 2026 \u00b7 2027', u'C# / .NET', u'9 herramientas']),
    h1=u'LMBIM<em>Tools</em>.',
    alt=u'LMBIMTools \u2014 Add-In de acero de refuerzo para Autodesk Revit',
    fb_kicker=u'Revit Add-In \u00b7 .NET',
    fb_titulo=u'LMBIM<em style=&quot;color: var(--accent); font-style: italic;&quot;>Tools</em>',
    pie_caratula=u'Complemento propio \u00b7 distribuci\u00f3n directa',
    parrafos=parrafos([
        u'LMBIMTools es la pesta\u00f1a <span style="color: var(--text);">LM BIM</span> que a\u00f1ado a Autodesk Revit: nueve herramientas escritas en C# sobre la API de Revit que se llevan el trabajo manual del acero de refuerzo. Selecciono las columnas, las vigas, las zapatas, los muros o las losas ya modeladas y el complemento genera los elementos <span style="color: var(--text);">Rebar</span> reales dentro del modelo \u2014no l\u00edneas de dibujo\u2014, con los espaciamientos, ganchos s\u00edsmicos y zonas de confinamiento que exige la norma peruana <span style="color: var(--text);">NTE E.060</span>.',
        u'Un solo c\u00f3digo fuente compila a dos DLLs por multi-targeting (.NET 8 para Revit 2025 y 2026, .NET 10 para Revit 2027), de modo que la suite entera se mantiene con una sola base de c\u00f3digo. Se instala con un micro-instalador propio en un \u00fanico EXE, sin permisos de administrador y sin dependencias externas: detecta las versiones de Revit presentes por registro y por carpeta de complementos, se detiene si Revit est\u00e1 abierto y publica las DLLs de forma at\u00f3mica. Todo el paquete va firmado digitalmente y el empaquetado aborta si la firma no queda v\u00e1lida.',
    ]),
    botones=botones([
        (u'Ver los servidores MCP', u'servidores-mcp.html', u'btn-outline', False),
        (u'Solicitar una demostraci\u00f3n', u'../index.html#contacto', u'btn-ghost', False),
    ]),
    specs=specs([
        (u'Categor\u00eda', u'Complemento BIM', u'Acero de refuerzo y detallado'),
        (u'Plataforma', u'Autodesk Revit', u'2025 \u00b7 2026 \u00b7 2027'),
        (u'Normativa', u'NTE E.060', u'Cat\u00e1logo peruano de barras'),
        (u'Distribuci\u00f3n', u'Instalador firmado', u'Sin permisos de administrador'),
    ]),
    titulo_a=u'Qu\u00e9 <em style="color: var(--accent); font-style:italic;">resuelve</em>',
    features=features([
        (u'Acero modelado, no dibujado', u'Las herramientas crean elementos Rebar, AreaReinforcement y PathReinforcement aut\u00e9nticos: cuantifican en las tablas de planificaci\u00f3n, se ven en 3D y viajan con el modelo.'),
        (u'La norma dentro del cuadro de di\u00e1logo', u'Los espaciamientos llegan precargados con el m\u00e1ximo de la E.060 para cada caso \u2014confinamiento de columnas, 2h en extremos de viga, bandeo de zapatas, dos capas en muros desde t = 200 mm\u2014 en lugar de dejarlos a criterio de quien modela.'),
        (u'Vista previa 2D antes de escribir en el modelo', u'Cada herramienta dibuja la secci\u00f3n armada en vivo mientras se ajustan di\u00e1metros y separaciones, de modo que el error se ve antes de tocar el proyecto.'),
        (u'Despiece y planos, no solo geometr\u00eda', u'Detallar Secci\u00f3n genera las vistas perpendiculares, las etiquetas de armadura y el cuadro de armado con notaci\u00f3n peruana, agrupando en una sola secci\u00f3n t\u00edpica los elementos con id\u00e9ntico armado.'),
        (u'Cat\u00e1logo peruano de una vez y para siempre', u'Tipos de Barra carga calibres de 6 mm a 1 3/8", ganchos s\u00edsmicos de 135\u00b0 y recubrimientos de E.060 \u00a77.7.1 de forma idempotente: ejecutarla dos veces no duplica nada.'),
        (u'Multi-versi\u00f3n sin bifurcar el c\u00f3digo', u'Una sola clase concentra las diferencias entre las APIs de 2025 y 2027; compilar contra la API m\u00e1s antigua hace que el compilador detecte solo cualquier uso incompatible.'),
    ]),
    titulo_b=u'Las nueve <em style="color: var(--accent); font-style:italic;">herramientas</em>',
    filas=filas([
        (u'Tipos de Barra', u'Carga en el proyecto el cat\u00e1logo peruano de acero de refuerzo: calibres de 6 mm a 1 3/8", ganchos s\u00edsmicos de 135\u00b0 y recubrimientos de E.060 \u00a77.7.1. Es prerrequisito del resto del panel y no duplica tipos al repetirse.'),
        (u'Acero en Columna', u'Refuerzo longitudinal y estribos con las tres zonas de confinamiento en las columnas seleccionadas, con espaciamientos precargados seg\u00fan E.060 \u00a721.6.4 (o \u00a721.4.5 en sistemas de muros).'),
        (u'Acero en Viga', u'Acero corrido, bastones y estribos con confinamiento 2h en ambos extremos. Los puntos de corte de los bastones se fijan como fracci\u00f3n de la luz libre o en mil\u00edmetros exactos.'),
        (u'Acero en Zapata', u'Parrilla inferior \u2014y superior opcional\u2014 m\u00e1s los arranques hacia la columna: bandeo de la direcci\u00f3n corta seg\u00fan E.060 \u00a715.4.4.2, anclaje por desarrollo en compresi\u00f3n (\u00a712.3.2) y empalme de arranques (\u00a712.16.1 o \u00a712.17.2.1).'),
        (u'Acero en Muro', u'Malla del alma en una o dos capas y elementos de borde confinados: cuant\u00edas m\u00ednimas de \u00a711.10.7 y \u00a714.3.1, dos capas desde t = 200 mm (\u00a721.9.4.3) y bordes con estribos s\u00edsmicos y ganchos est\u00e1ndar (\u00a721.9.7).'),
        (u'Acero en Losa', u'Parrilla de losas macizas y plateas, m\u00e1s los bastones de momento negativo en los bordes: cuant\u00eda m\u00ednima por retracci\u00f3n y temperatura (\u00a79.7.2), espaciamientos de 3\u00b7t o 400 mm (\u00a79.7.3) y 2\u00b7t en secciones cr\u00edticas (\u00a713.3.2).'),
        (u'Detallar Secci\u00f3n', u'Documentaci\u00f3n de despiece de columnas y vigas ya armadas: secciones perpendiculares, etiquetas de armadura, cuadro de armado con notaci\u00f3n peruana y composici\u00f3n en el plano, con una sola secci\u00f3n t\u00edpica por armado repetido.'),
        (u'Colorear Refuerzo', u'Colorea las barras de la vista activa por di\u00e1metro o por funci\u00f3n \u2014estribo, longitudinal, bast\u00f3n, arranque\u2014 mediante sobrescrituras gr\u00e1ficas: no toca el modelo y se revierte con un clic.'),
        (u'Ajustar Recorte', u'Ajusta la regi\u00f3n de recorte de la vista activa, o de todas las secciones seleccionadas, a los l\u00edmites reales de la geometr\u00eda del modelo.'),
    ]),
    kicker_c=u'Por qu\u00e9 lo constru\u00ed',
    titulo_c=u'El acero es donde el modelo BIM<br><em>se cae o se sostiene</em>.',
    cierre=cierre([
        u'En la pr\u00e1ctica, casi ning\u00fan proyecto llega a modelar el refuerzo: se dibuja en 2D aparte, se cuantifica a mano y el modelo deja de ser la fuente \u00fanica de verdad justo en la partida que m\u00e1s pesa en el presupuesto. Modelarlo a mano en Revit es posible, pero tan lento que nadie lo sostiene bajo plazo de expediente.',
        u'LMBIMTools ataca exactamente ese cuello de botella. La decisi\u00f3n de dise\u00f1o de fondo es que la norma viva en el c\u00f3digo y no en la memoria de quien modela: los valores de E.060 llegan cargados por defecto en cada di\u00e1logo, y quien modela decide cu\u00e1ndo apartarse de ellos, no cu\u00e1ndo recordarlos.',
        u'La suite crece por registro declarativo: cada herramienta nueva es una carpeta y una entrada en una lista, con el n\u00facleo de geometr\u00eda y norma separado de la API de Revit para que pueda probarse sin abrir el programa. Es la misma disciplina con la que desarrollo el resto del ecosistema.',
    ]),
))

# ─────────────────────────────────────────────────────────────────────────
# 2. Servidores MCP
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'servidores-mcp',
    img=u'servidores_mcp',
    title=u'Servidores MCP \u2014 Delphin, Word y Excel para agentes de IA \u00b7 Luis Miguel Cruz Efus',
    desc=u'Tres servidores MCP (Model Context Protocol) de desarrollo propio y ejecuci\u00f3n local: delphin-presupuestos con 27 herramientas sobre la base SQLite de Delphin Express, m\u00e1s Word MCP y Excel MCP para entregables con maquetaci\u00f3n profesional.',
    navlabel=u'IA.02 \u00b7 Model Context Protocol',
    footlabel=u'IA.02 \u00b7 Servidores MCP',
    coord_izq=u'IA.02 / Model Context Protocol',
    coord_der=u'3 servidores \u00b7 39 herramientas \u00b7 Ejecuci\u00f3n local',
    chips=chips([u'Desarrollo propio', u'Model Context Protocol', u'Python', u'39 herramientas']),
    h1=u'Servidores <em>MCP</em>.',
    alt=u'Suite de servidores MCP \u2014 Delphin, Word y Excel',
    fb_kicker=u'Model Context Protocol',
    fb_titulo=u'Servidores <em style=&quot;color: var(--accent); font-style: italic;&quot;>MCP</em>',
    pie_caratula=u'Infraestructura propia \u00b7 uso interno',
    parrafos=parrafos([
        u'Un modelo de lenguaje sabe redactar, pero no sabe tocar tus archivos. El <span style="color: var(--text);">Model Context Protocol</span> es el est\u00e1ndar por el que un agente de IA recibe herramientas concretas, y estos tres servidores son las que yo le doy: <span style="color: var(--text);">delphin-presupuestos</span>, que abre la base SQLite de Delphin Express con 27 herramientas; <span style="color: var(--text);">Word MCP</span> y <span style="color: var(--text);">Excel MCP</span>, que producen los entregables ya maquetados. Los tres corren en mi propia m\u00e1quina, sobre mis propios datos, sin subir nada a la nube.',
        u'La regla de dise\u00f1o es la misma en los tres: <span style="color: var(--text);">el agente describe el contenido y el servidor decide la presentaci\u00f3n</span>. No hay par\u00e1metros para elegir tipograf\u00eda, color ni bordes, y es deliberado \u2014si el agente pudiera elegirlos, los elegir\u00eda mal, que es justamente el problema que estos servidores existen para eliminar. Lo mismo vale para los datos: las herramientas de presupuesto se niegan a inventar rendimientos o precios que ya est\u00e1n en el cat\u00e1logo.',
    ]),
    botones=botones([
        (u'Ver el pipeline de presupuestos', u'automatizacion-presupuestos.html', u'btn-outline', False),
        (u'Conversemos sobre integraci\u00f3n', u'../index.html#contacto', u'btn-ghost', False),
    ]),
    specs=specs([
        (u'Categor\u00eda', u'Infraestructura de IA', u'Herramientas para agentes'),
        (u'Protocolo', u'Model Context Protocol', u'Claude Code \u00b7 OpenCode \u00b7 Antigravity'),
        (u'Alcance', u'3 servidores', u'39 herramientas expuestas'),
        (u'Ejecuci\u00f3n', u'100 % local', u'Sin env\u00edo de datos a la nube'),
    ]),
    titulo_a=u'Qu\u00e9 <em style="color: var(--accent); font-style:italic;">resuelven</em>',
    features=features([
        (u'Presupuestos sin salir del agente', u'delphin-presupuestos consulta el banco de APUs, valida, crea el presupuesto en la base de Delphin Express y lo corrige en sitio, con respaldo numerado antes de cada escritura.'),
        (u'Ninguna cifra inventada', u'Los rendimientos salen del APU y los precios del cat\u00e1logo. Solo un insumo verdaderamente nuevo admite precio estimado, y debe declarar de d\u00f3nde sale.'),
        (u'Correcci\u00f3n en sitio, nunca regeneraci\u00f3n', u'Regenerar un presupuesto cambia los identificadores de costo unitario y con ellos se pierden los metrados de las planillas y las dependencias del cronograma. Por eso las herramientas de edici\u00f3n existen y el servidor empuja hacia ellas.'),
        (u'Maquetaci\u00f3n que el agente no puede estropear', u'Word MCP aplica jerarqu\u00eda de t\u00edtulos, cabeceras sombreadas que se repiten entre p\u00e1ginas, columnas num\u00e9ricas alineadas y pie con \u00abP\u00e1gina X de Y\u00bb, siempre igual en todo el documento.'),
        (u'Numeraci\u00f3n que se recoloca sola', u'Las leyendas de tabla y figura se insertan con campo SEQ, como lo hace Word: si se a\u00f1ade una tabla en medio, el resto se renumera solo en lugar de romperse.'),
        (u'Hojas de c\u00e1lculo vivas, no capturas', u'Excel MCP entrega libros con ancho de columna ajustado, formato num\u00e9rico real, cabecera fija con autofiltro, fila de totales con SUBTOTAL que respeta el filtro y gr\u00e1ficos rotulados.'),
    ]),
    titulo_b=u'Los tres <em style="color: var(--accent); font-style:italic;">servidores</em>',
    filas=filas([
        (u'delphin-presupuestos \u00b7 27 herramientas', u'Trabaja directamente sobre las bases SQLite de Delphin Express. Consulta y compara APUs, busca insumos y precios de referencia, valida e inyecta presupuestos completos, edita partidas una a una, carga metrados desde planillas, ordena las carpetas del cat\u00e1logo, cuida el banco de APUs (duplicados, fusiones, altas) y verifica la base antes de abrirla. Respalda de forma numerada antes de cada escritura y se niega a escribir si Delphin est\u00e1 abierto.'),
        (u'Word MCP \u00b7 6 herramientas', u'Crea el documento entero de una sola llamada a partir de bloques \u2014t\u00edtulos, p\u00e1rrafos, tablas, listas, im\u00e1genes, \u00edndice, citas\u2014 y aplica por su cuenta tipograf\u00eda, sombreados, bordes y espaciados. Tambi\u00e9n lee un .docx existente devolvi\u00e9ndolo en el mismo formato que acepta para crearlo, y rellena plantillas del cliente por reemplazo sin destrozar su encabezado ni su logo.'),
        (u'Excel MCP \u00b7 6 herramientas', u'Crea el libro completo de una llamada: hojas con t\u00edtulo, encabezados, filas, formatos por columna y gr\u00e1ficos declarados por nombre de columna. Exige los n\u00fameros como n\u00fameros y no como texto, que es el error que m\u00e1s estropea una hoja, y sabe dejar f\u00f3rmulas vivas para plantillas de c\u00e1lculo.'),
    ]),
    kicker_c=u'Por qu\u00e9 los constru\u00ed',
    titulo_c=u'Los agentes redactan bien<br>y <em>maquetan mal</em>.',
    cierre=cierre([
        u'No es falta de capacidad del modelo: maquetar exige acordarse de treinta detalles que nadie tiene en la cabeza mientras redacta. Los s\u00edntomas siempre son los mismos \u2014tablas con la rejilla negra de Word, \u00edndices escritos como texto que no se actualizan, leyendas \u00abTabla 1\u00bb escritas a mano que se rompen a la primera inserci\u00f3n, n\u00fameros como 1234.5599999999999 alineados a la izquierda y, lo peor, plantillas del cliente destrozadas.',
        u'La soluci\u00f3n no fue pedirle al agente que maquetara mejor, sino quitarle esa decisi\u00f3n: el servidor se queda con toda la presentaci\u00f3n y el agente aporta \u00fanicamente estructura y contenido. Deliberadamente no expongo par\u00e1metros visuales; la ausencia de esa palanca es la caracter\u00edstica, no una limitaci\u00f3n.',
        u'Con delphin-presupuestos la misma idea se aplica a los datos duros. Un presupuesto de obra p\u00fablica no admite cifras plausibles: admite las del cat\u00e1logo. El servidor impone esa disciplina desde el otro lado \u2014base de solo lectura donde debe serlo, respaldo antes de escribir, negativa a operar con Delphin abierto\u2014 para que la velocidad de la IA nunca se pague con trazabilidad.',
    ]),
))

# ─────────────────────────────────────────────────────────────────────────
# 3. Automatizacion de presupuestos
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'automatizacion-presupuestos',
    img=u'automatizacion_presupuestos',
    title=u'Automatizaci\u00f3n de presupuestos y entregables de obra \u00b7 Luis Miguel Cruz Efus',
    desc=u'Pipeline propio en Python e IA que genera presupuestos contra un banco de 3 002 APUs, los inyecta en Delphin Express, deriva el cronograma CPM de los rendimientos y produce fletes, especificaciones t\u00e9cnicas y cotizaciones.',
    navlabel=u'IA.03 \u00b7 Costos y entregables',
    footlabel=u'IA.03 \u00b7 Automatizaci\u00f3n de presupuestos',
    coord_izq=u'IA.03 / Costos y entregables',
    coord_der=u'Python \u00b7 SQLite \u00b7 Delphin Express \u00b7 CPM',
    chips=chips([u'Desarrollo propio', u'Delphin Express / SQLite', u'Banco de 3 002 APUs', u'Cronograma CPM']),
    h1=u'Presupuestos<br><em>automatizados</em>.',
    alt=u'Automatizaci\u00f3n de presupuestos y entregables de obra',
    fb_kicker=u'Pipeline Python + IA',
    fb_titulo=u'Presupuestos <em style=&quot;color: var(--accent); font-style: italic;&quot;>autom\u00e1ticos</em>',
    pie_caratula=u'Sistema interno \u00b7 saneamiento rural',
    parrafos=parrafos([
        u'Un expediente t\u00e9cnico no termina en el presupuesto: termina en el presupuesto <em>y</em> el cronograma, <em>y</em> las especificaciones t\u00e9cnicas, <em>y</em> el flete, <em>y</em> las cotizaciones que sustentan cada precio. Este sistema los produce en cadena desde una sola fuente \u2014la base <span style="color: var(--text);">SQLite de Delphin Express</span> del proyecto\u2014 combinando Python para lo determinista con IA para lo que exige criterio.',
        u'El coraz\u00f3n es un banco propio de <span style="color: var(--text);">3 002 an\u00e1lisis de precios unitarios</span> organizados en 25 grupos de costo, construido a partir de expedientes reales de saneamiento. La IA no inventa rendimientos: los busca ah\u00ed. Cada escritura sobre una base de Delphin va precedida de un respaldo numerado, la base original nunca se modifica y el resultado se verifica antes de abrirlo en el programa.',
    ]),
    botones=botones([
        (u'Ver los servidores MCP que lo operan', u'servidores-mcp.html', u'btn-outline', False),
        (u'Conversemos sobre tu expediente', u'../index.html#contacto', u'btn-ghost', False),
    ]),
    specs=specs([
        (u'Categor\u00eda', u'Ingenier\u00eda de costos', u'Expedientes de saneamiento'),
        (u'Motor', u'Python + IA', u'Sobre SQLite de Delphin Express'),
        (u'Banco de datos', u'3 002 APUs', u'25 grupos de costo'),
        (u'Entregables', u'5 productos en cadena', u'Presupuesto \u00b7 CPM \u00b7 EETT \u00b7 flete \u00b7 precios'),
    ]),
    titulo_a=u'Qu\u00e9 <em style="color: var(--accent); font-style:italic;">automatiza</em>',
    features=features([
        (u'Presupuesto inyectado, no transcrito', u'El presupuesto se valida en un formato intermedio y se escribe directamente en la base de Delphin Express. Validado de extremo a extremo en el programa real, no en una exportaci\u00f3n.'),
        (u'Cronograma CPM desde los rendimientos', u'Las duraciones se despejan del propio APU, la secuencia constructiva la razona la IA y el plazo se comprime al contractual. Un solo comando copia la base, secuencia, calcula el CPM, ajusta, inyecta y verifica.'),
        (u'El cronograma vive dentro de Delphin', u'Se escribe en la misma base, de modo que su m\u00f3dulo CPM lo reproduce al 100 % y exporta a MS Project por su cuenta. Sin doble digitaci\u00f3n ni desincronizaci\u00f3n entre archivos.'),
        (u'Especificaciones t\u00e9cnicas desde las partidas', u'Una biblioteca de plantillas por c\u00f3digo de partida, con las cinco secciones est\u00e1ndar, se cruza con el presupuesto y produce el documento Word listo para imprimir; lo que no tiene plantilla se redacta con IA y queda marcado para revisi\u00f3n.'),
        (u'Flete terrestre y rural en Excel', u'Genera el Excel de flete con f\u00f3rmulas vinculadas y formato A4 imprimible, con tarifas por tipo de v\u00eda y factor de retorno vac\u00edo centralizadas en un \u00fanico archivo de configuraci\u00f3n.'),
        (u'Trazabilidad como requisito, no como extra', u'Respaldo numerado antes de cada escritura, bases maestras de solo lectura, negativa a operar con Delphin abierto y verificaci\u00f3n posterior de la base resultante.'),
    ]),
    titulo_b=u'Los <em style="color: var(--accent); font-style:italic;">m\u00f3dulos</em> del pipeline',
    filas=filas([
        (u'N\u00facleo de datos', u'Base maestra de Delphin, diccionarios de conocimiento \u2014rendimientos, pesos y vol\u00famenes unitarios\u2014 y los esquemas del formato intermedio. Es la \u00fanica fuente de verdad del sistema y se mantiene de solo lectura.'),
        (u'Banco de APUs', u'3 002 an\u00e1lisis de precios unitarios en 25 grupos de costo, desde obras provisionales y movimiento de tierras hasta tuber\u00edas de saneamiento, plantas de tratamiento y fletes. Se cuida con herramientas propias de estad\u00edstica, detecci\u00f3n de duplicados, comparaci\u00f3n y fusi\u00f3n.'),
        (u'M\u00f3dulo de presupuestos', u'IA \u2192 presupuesto en formato intermedio \u2192 validador \u2192 inyector \u2192 base de Delphin. El validador es una compuerta: si no sale limpio, no se crea nada.'),
        (u'M\u00f3dulo de cronogramas', u'Duraciones desde los APUs, secuencia constructiva razonada por IA, CPM calculado y comprimido al plazo contractual, e inyectado dentro de la misma base de Delphin.'),
        (u'M\u00f3dulo de especificaciones', u'Plantillas en Markdown por c\u00f3digo de partida con frontmatter y las cinco secciones normativas \u2014descripci\u00f3n, materiales, m\u00e9todo de ejecuci\u00f3n, m\u00e9todo de medici\u00f3n y forma de pago\u2014 que se ensamblan en el Word final.'),
        (u'M\u00f3dulo de fletes', u'Extrae materiales y cantidades del presupuesto, los cruza con el diccionario de pesos y vol\u00famenes y emite el Excel de flete con f\u00f3rmulas vinculadas.'),
        (u'M\u00f3dulo de cotizaciones', u'Solicitud y clasificaci\u00f3n de cotizaciones para mantener los precios vivos con trazabilidad de su origen.'),
    ]),
    kicker_c=u'Por qu\u00e9 lo constru\u00ed',
    titulo_c=u'El expediente se atasca<br>en <em>lo repetitivo</em>.',
    cierre=cierre([
        u'La parte dif\u00edcil de un expediente de saneamiento no es la que consume el tiempo. El criterio \u2014qu\u00e9 tecnolog\u00eda, qu\u00e9 secuencia constructiva, qu\u00e9 partidas\u2014 se decide relativamente r\u00e1pido; lo que devora las semanas es transcribir ese criterio a cinco documentos distintos y mantenerlos cuadrados entre s\u00ed cuando algo cambia.',
        u'Por eso el sistema no parte de una plantilla en blanco sino de la base de datos del proyecto: si el presupuesto cambia, el cronograma, el flete y las especificaciones se vuelven a derivar de la misma fuente en lugar de corregirse a mano uno por uno. Ah\u00ed es donde se van los reprocesos y las observaciones por incoherencias entre tomos.',
        u'La divisi\u00f3n del trabajo es expl\u00edcita: Python para lo que tiene una respuesta correcta \u2014aritm\u00e9tica, CPM, formato, escritura en la base\u2014 e IA para lo que exige criterio \u2014secuencia constructiva, redacci\u00f3n de una especificaci\u00f3n sin plantilla, clasificaci\u00f3n de cotizaciones\u2014. Y todo lo que la IA propone queda marcado como propuesta hasta que un ingeniero lo firma.',
    ]),
))

# ─────────────────────────────────────────────────────────────────────────
# 4. Agentes de IA
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'agentes-ia',
    img=u'agentes_ia',
    title=u'Ecosistema de agentes de inteligencia artificial \u00b7 Luis Miguel Cruz Efus',
    desc=u'Agente aut\u00f3nomo de licitaciones de desarrollo propio: rastrea las convocatorias del SEACE, descarga y lee con IA las bases administrativas y los t\u00e9rminos de referencia, y los contrasta contra el perfil real del equipo para emitir un informe de viabilidad.',
    navlabel=u'IA.04 \u00b7 Agentes aut\u00f3nomos',
    footlabel=u'IA.04 \u00b7 Agentes de IA',
    coord_izq=u'IA.04 / Agentes aut\u00f3nomos',
    coord_der=u'Python \u00b7 Gemini \u00b7 SEACE \u00b7 Ejecuci\u00f3n local',
    chips=chips([u'Desarrollo propio', u'Agentes aut\u00f3nomos', u'SEACE', u'Ejecuci\u00f3n local']),
    h1=u'Agentes<br><em>aut\u00f3nomos</em>.',
    alt=u'Ecosistema de agentes de inteligencia artificial',
    fb_kicker=u'AI Agents',
    fb_titulo=u'Agentes <em style=&quot;color: var(--accent); font-style: italic;&quot;>aut\u00f3nomos</em>',
    pie_caratula=u'Sistemas internos \u00b7 uso propio',
    parrafos=parrafos([
        u'Un agente no es un chat: es un programa que persigue un objetivo por su cuenta \u2014consulta fuentes, descarga archivos, los lee y responde una pregunta concreta\u2014 sin que nadie le d\u00e9 el siguiente paso. Construyo agentes para las tareas que hay que hacer <span style="color: var(--text);">todos los d\u00edas</span>, siempre igual, y que nadie quiere hacer todos los d\u00edas.',
        u'El que sostengo en producci\u00f3n para el trabajo de consultor\u00eda vigila el <span style="color: var(--text);">SEACE</span>, el portal de contrataciones del Estado peruano. La arquitectura es la que repito en todos: orquestador en Python, modelo de lenguaje para la parte de juicio, panel web propio para operarlo y el criterio de decisi\u00f3n escrito en un archivo, no improvisado en cada consulta. Corre en mi m\u00e1quina; las bases descargadas y el perfil del equipo no salen de ah\u00ed.',
    ]),
    botones=botones([
        (u'Ver los servidores MCP', u'servidores-mcp.html', u'btn-outline', False),
        (u'Conversemos sobre automatizaci\u00f3n', u'../index.html#contacto', u'btn-ghost', False),
    ]),
    specs=specs([
        (u'Categor\u00eda', u'Agente aut\u00f3nomo', u'Orquestaci\u00f3n en Python'),
        (u'Fuente', u'Portal SEACE', u'Contrataciones del Estado'),
        (u'Entregable', u'Informe de viabilidad', u'Una decisi\u00f3n por convocatoria'),
        (u'Ejecuci\u00f3n', u'100 % local', u'Panel web propio'),
    ]),
    titulo_a=u'Qu\u00e9 <em style="color: var(--accent); font-style:italic;">hace solo</em>',
    features=features([
        (u'Busca en la fuente, no en una copia', u'Consulta el buscador del SEACE, lista los archivos de cada convocatoria y descarga los PDF de bases y t\u00e9rminos de referencia directamente del portal.'),
        (u'Lee documentos largos y extrae lo que decide', u'Los PDF se analizan con un modelo de lenguaje para sacar requisitos, plazos, experiencia exigida y condiciones, en lugar de leerlos completos a mano.'),
        (u'Contrasta contra el perfil real del equipo', u'El resultado se compara con la experiencia documentada \u2014proyectos, especialidades, colegiatura\u2014 para responder la \u00fanica pregunta que importa: si vale la pena presentarse.'),
        (u'Descarta antes que maquillar', u'El perfil del equipo lleva escrita la regla de honestidad: no estirar fechas, no redondear a\u00f1os hacia arriba, no forzar equivalencias de tipolog\u00eda de obra. Si falta un requisito, el informe lo dice y recomienda no presentarse.'),
        (u'Un informe por convocatoria, archivado', u'Cada an\u00e1lisis queda guardado y consultable desde el panel, de modo que la decisi\u00f3n de no presentarse tambi\u00e9n deja rastro y no se vuelve a evaluar dos veces lo mismo.'),
        (u'El modelo se elige seg\u00fan el documento', u'La lista de modelos disponibles se consulta en vivo y se puede analizar tanto un PDF descargado a mano como uno tra\u00eddo directamente del portal.'),
    ]),
    titulo_b=u'C\u00f3mo <em style="color: var(--accent); font-style:italic;">trabaja</em>',
    filas=filas([
        (u'Agente de licitaciones (SEACE)', u'Busca convocatorias en el portal del SEACE, lista y descarga los PDF de bases administrativas y t\u00e9rminos de referencia, los analiza con un modelo de lenguaje y contrasta los requisitos contra el perfil documentado del equipo. Entrega un informe de viabilidad por convocatoria y conserva los reportes generados. Se opera desde un panel web local, con selecci\u00f3n de modelo y an\u00e1lisis tanto de PDF locales como tra\u00eddos del portal.'),
        (u'El criterio, escrito una sola vez', u'El perfil del equipo vive en un archivo versionado \u2014experiencia laboral con fechas exactas, colegiatura, tipolog\u00edas de obra ejecutadas\u2014 y solo se modifica cuando hay un avance real y demostrable. Ah\u00ed est\u00e1 tambi\u00e9n la regla dura: nada de estirar fechas ni de forzar equivalencias para que un requisito encaje. El agente aplica ese criterio igual la primera vez que la mil\u00e9sima.'),
        (u'Arquitectura y operaci\u00f3n', u'Orquestador en Python con interfaz de l\u00ednea de comandos y panel web propio; cada etapa \u2014buscar, descargar, leer, contrastar, informar\u2014 se ejecuta por separado para poder depurarla. Rutas relativas en todo el c\u00f3digo, rotaci\u00f3n de claves de API y ejecuci\u00f3n \u00edntegra en local: ni las bases descargadas ni el perfil del equipo salen de la m\u00e1quina.'),
        (u'El resto del ecosistema', u'Con la misma arquitectura opero agentes internos de soporte al desarrollo \u2014auditor\u00eda de mis propias aplicaciones contra la norma, empaquetado y publicaci\u00f3n de versiones, transcripci\u00f3n de bibliograf\u00eda t\u00e9cnica\u2014. No son producto: son la infraestructura con la que se sostiene todo lo dem\u00e1s de esta secci\u00f3n.'),
    ]),
    kicker_c=u'Por qu\u00e9 los constru\u00ed',
    titulo_c=u'La vigilancia diaria<br>es <em>trabajo de m\u00e1quina</em>.',
    cierre=cierre([
        u'Revisar el SEACE a diario es una tarea que ninguna consultora peque\u00f1a puede sostener bien: se hace a rachas, se revisa por encima y las convocatorias que encajaban se descubren cuando ya venci\u00f3 el plazo. No es un problema de criterio \u2014el criterio para descartar una convocatoria est\u00e1 claro\u2014 sino de constancia.',
        u'Esa es exactamente la forma de un agente: objetivo estable, fuente fija, criterio escrito una vez y ejecuci\u00f3n sin cansancio. Lo que la IA aporta ah\u00ed no es creatividad, es lectura incansable de documentos largos y la capacidad de responder siempre la misma pregunta con el mismo est\u00e1ndar.',
        u'El l\u00edmite est\u00e1 puesto a prop\u00f3sito: el agente busca, lee, contrasta y recomienda, pero la decisi\u00f3n queda del lado humano. No se presenta a ninguna licitaci\u00f3n ni firma nada. Automatizo el trabajo previo a la decisi\u00f3n, no la decisi\u00f3n.',
    ]),
))


if not os.path.isdir(DEST):
    os.makedirs(DEST)

for pg in PAGINAS:
    html = CABECERA.format(**pg)
    ruta = os.path.join(DEST, pg['slug'] + u'.html')
    io.open(ruta, 'w', encoding='utf-8', newline='\n').write(html)
    print(u'OK  %-34s %6d bytes' % (pg['slug'] + u'.html', len(html.encode('utf-8'))))
