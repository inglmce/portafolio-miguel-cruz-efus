# -*- coding: utf-8 -*-
"""Genera las 4 fichas de la seccion IA & Automatizacion del portafolio."""
import io, os
from pathlib import Path

DEST = Path(__file__).resolve().parent.parent / "ia"

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
<meta property="og:image" content="https://luismiguelcruzefus.com/imagenes/lm_ingenieria/{img}/00_caratula.webp">
<meta property="og:locale" content="es_PE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://luismiguelcruzefus.com/imagenes/lm_ingenieria/{img}/00_caratula.webp">

<link rel="icon" type="image/webp" href="../imagenes/lm_ingenieria/marca_lm/LOGO.webp">

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
          <img src="../imagenes/lm_ingenieria/{img}/00_caratula.webp" alt="{alt}" onerror="this.style.display='none'; this.parentElement.insertAdjacentHTML('beforeend', '<div class=&quot;fallback&quot;><div><div class=&quot;mono text-[0.62rem] uppercase tracking-[0.18em] mb-3&quot; style=&quot;color: var(--accent);&quot;>{fb_kicker}</div><div class=&quot;serif text-3xl leading-tight&quot;>{fb_titulo}</div></div></div>');">
        </div>
        <p class="mono text-[0.66rem] uppercase tracking-[0.14em] mt-4 text-center" style="color: var(--muted);">{pie_caratula}</p>
      </div>
    </div>

    <div class="spec-strip mt-14" data-reveal>
{specs}
    </div>
  </div>
</section>

<!-- SECCION B -->
<section class="py-20 lg:py-28 border-t" style="border-color: var(--line-soft);">
  <div class="max-w-7xl mx-auto px-6 lg:px-10">

    <div class="flex items-baseline gap-5 mb-10">
      <span class="mono text-sm" style="color: var(--accent);">\u00a7 A</span>
      <h2 class="serif text-3xl lg:text-4xl">{titulo_b}</h2>
    </div>

    <div class="mt-2">
{filas}
    </div>
  </div>
</section>

<!-- CTA -->
<section class="py-24 lg:py-32 relative overflow-hidden">
  <div class="absolute inset-0 blueprint-bg" style="opacity:0.3"></div>
  <div class="max-w-5xl mx-auto px-6 lg:px-10 relative text-center">
    <div class="coord justify-center mb-8" style="display:inline-flex;">N.99 \u00b7 M\u00e1s desarrollo propio</div>
    <h2 class="display text-4xl md:text-5xl mb-10">
      M\u00e1s <em>automatizaci\u00f3n</em>.
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
    desc='Complemento para Autodesk Revit con nueve herramientas de modelado de acero de refuerzo, secciones y despiece.',
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
        'Desarrollo LMBIMTools, un complemento para Revit con nueve herramientas para modelar el acero de columnas, vigas, zapatas, muros y losas, y preparar su despiece.',
        'Es compatible con Revit 2025, 2026 y 2027. Se distribuye mediante un instalador firmado que detecta las versiones instaladas.',
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
    titulo_b=u'Las nueve <em style="color: var(--accent); font-style:italic;">herramientas</em>',
    filas=filas([
        ('Tipos de Barra', 'Carga el catálogo peruano de barras, ganchos sísmicos y recubrimientos. Conserva los tipos ya existentes.'),
        ('Acero en Columna', 'Genera refuerzo longitudinal y estribos con zonas de confinamiento en las columnas seleccionadas.'),
        ('Acero en Viga', 'Modela acero corrido, bastones y estribos. Permite definir los cortes de barras por longitud o fracción de la luz.'),
        ('Acero en Zapata', 'Genera parrillas inferiores, refuerzo superior opcional y arranques de columna.'),
        ('Acero en Muro', 'Modela la malla del alma en una o dos capas y los elementos de borde confinados.'),
        ('Acero en Losa', 'Genera parrillas en losas macizas y plateas, con bastones de momento negativo en los bordes.'),
        ('Detallar Sección', 'Crea secciones, etiquetas y cuadros de armado de columnas y vigas. Agrupa elementos con el mismo refuerzo.'),
        ('Colorear Refuerzo', 'Asigna colores por diámetro o función de la barra en la vista activa. Los cambios gráficos se pueden revertir.'),
        ('Ajustar Recorte', 'Ajusta el recorte de las vistas a los límites de la geometría del modelo.'),
    ]),
))

# ─────────────────────────────────────────────────────────────────────────
# 2. Servidores MCP
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'servidores-mcp',
    img=u'servidores_mcp',
    title=u'Servidores MCP \u2014 Delphin, Word y Excel para agentes de IA \u00b7 Luis Miguel Cruz Efus',
    desc='Tres servidores MCP para trabajar con presupuestos de Delphin Express, documentos Word y libros Excel mediante agentes de IA.',
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
        'Desarrollo tres servidores MCP para conectar agentes de IA con Delphin Express, Word y Excel. Reúnen 39 herramientas para consultar presupuestos y preparar entregables.',
        'El agente aporta el contenido; los servidores aplican el formato del documento y las reglas de edición de los datos.',
    ]),
    botones=botones([
        (u'Ver automatizaci\u00f3n de presupuestos', u'automatizacion-presupuestos.html', u'btn-outline', False),
        (u'Conversemos sobre integraci\u00f3n', u'../index.html#contacto', u'btn-ghost', False),
    ]),
    specs=specs([
        (u'Categor\u00eda', u'Infraestructura de IA', u'Herramientas para agentes'),
        (u'Protocolo', u'Model Context Protocol', u'Claude Code \u00b7 OpenCode \u00b7 Antigravity'),
        (u'Alcance', u'3 servidores', u'39 herramientas expuestas'),
        (u'Ejecuci\u00f3n', u'100 % local', u'Sin env\u00edo de datos a la nube'),
    ]),
    titulo_b=u'Los tres <em style="color: var(--accent); font-style:italic;">servidores</em>',
    filas=filas([
        ('delphin-presupuestos · 27 herramientas', 'Consulta APUs e insumos, crea y edita presupuestos, carga metrados y verifica bases SQLite de Delphin Express. Genera un respaldo antes de escribir y comprueba que Delphin esté cerrado.'),
        ('Word MCP · 6 herramientas', 'Crea documentos con títulos, tablas, imágenes, índices y citas. También lee documentos existentes y rellena plantillas conservando encabezados y logotipos.'),
        ('Excel MCP · 6 herramientas', 'Crea libros con formatos numéricos, fórmulas, filtros, totales y gráficos. Ajusta las columnas y conserva los números como valores de cálculo.'),
    ]),
))

# ─────────────────────────────────────────────────────────────────────────
# 3. Automatizacion de presupuestos
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'automatizacion-presupuestos',
    img=u'automatizacion_presupuestos',
    title=u'Automatizaci\u00f3n de presupuestos y entregables de obra \u00b7 Luis Miguel Cruz Efus',
    desc='Sistema para preparar presupuestos en Delphin Express, cronogramas CPM, especificaciones técnicas y hojas de flete.',
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
        'Desarrollé un sistema que prepara presupuestos, cronogramas, especificaciones técnicas y fletes a partir de la base de Delphin Express del proyecto.',
        'Usa un banco propio de 3 002 APUs, organizado en 25 grupos de costo. Python ejecuta los cálculos y la escritura de datos; la IA propone secuencias constructivas y redacta textos para revisión.',
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
    titulo_b=u'Los <em style="color: var(--accent); font-style:italic;">m\u00f3dulos</em> del pipeline',
    filas=filas([
        ('Núcleo de datos', 'Base maestra de Delphin y diccionarios de rendimientos, pesos y volúmenes unitarios, conservados como fuentes de consulta.'),
        ('Banco de APUs', '3 002 análisis de precios unitarios de expedientes de saneamiento, con herramientas de comparación, detección de duplicados y fusión.'),
        ('Presupuestos', 'Valida las partidas y escribe el presupuesto en una copia de la base de Delphin. Verifica el resultado antes de abrirlo.'),
        ('Cronogramas', 'Calcula duraciones desde los APUs y el CPM a partir de la secuencia propuesta. Ajusta el plazo e incorpora el cronograma en Delphin.'),
        ('Especificaciones técnicas', 'Ensambla un documento Word desde plantillas por código de partida. Los textos propuestos por IA quedan señalados para revisión.'),
        ('Fletes', 'Cruza las cantidades de materiales con sus pesos y volúmenes y genera un archivo Excel con fórmulas vinculadas.'),
        ('Cotizaciones', 'Organiza las cotizaciones y registra el origen de los precios de referencia.'),
    ]),
))

# ─────────────────────────────────────────────────────────────────────────
# 4. Agentes de IA
# ─────────────────────────────────────────────────────────────────────────
PAGINAS.append(dict(
    slug=u'agentes-ia',
    img=u'agentes_ia',
    title=u'Agentes de inteligencia artificial \u00b7 Luis Miguel Cruz Efus',
    desc='Agentes de IA para consultar convocatorias del SEACE, analizar bases y contrastar requisitos con la experiencia del equipo.',
    navlabel=u'IA.04 \u00b7 Agentes aut\u00f3nomos',
    footlabel=u'IA.04 \u00b7 Agentes de IA',
    coord_izq=u'IA.04 / Agentes aut\u00f3nomos',
    coord_der=u'Python \u00b7 Gemini \u00b7 SEACE \u00b7 Ejecuci\u00f3n local',
    chips=chips([u'Desarrollo propio', u'Agentes aut\u00f3nomos', u'SEACE', u'Ejecuci\u00f3n local']),
    h1=u'Agentes<br><em>aut\u00f3nomos</em>.',
    alt=u'Agentes de inteligencia artificial',
    fb_kicker=u'AI Agents',
    fb_titulo=u'Agentes <em style=&quot;color: var(--accent); font-style: italic;&quot;>aut\u00f3nomos</em>',
    pie_caratula=u'Sistemas internos \u00b7 uso propio',
    parrafos=parrafos([
        'Desarrollo agentes de IA para revisar convocatorias y documentos técnicos. El agente de licitaciones consulta el SEACE, descarga bases y TDR y compara los requisitos con la experiencia documentada del equipo.',
        'Los análisis se consultan desde un panel web. El agente prepara un informe por convocatoria; el equipo decide si se presenta.',
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
    titulo_b=u'C\u00f3mo <em style="color: var(--accent); font-style:italic;">trabaja</em>',
    filas=filas([
        ('Consulta del SEACE', 'Busca convocatorias y descarga las bases administrativas y los términos de referencia desde el portal.'),
        ('Análisis de requisitos', 'Identifica plazos, experiencia exigida y condiciones, y los compara con el perfil documentado del equipo. Señala los requisitos que no se cumplen.'),
        ('Informes y seguimiento', 'Guarda un informe por convocatoria para consultar el análisis y evitar revisiones duplicadas.'),
        ('Otras tareas', 'También uso agentes para revisar aplicaciones, preparar versiones y transcribir bibliografía técnica.'),
    ]),
))


if not os.path.isdir(DEST):
    os.makedirs(DEST)

for pg in PAGINAS:
    html = CABECERA.format(**pg)
    ruta = os.path.join(DEST, pg['slug'] + u'.html')
    io.open(ruta, 'w', encoding='utf-8', newline='\n').write(html)
    print(u'OK  %-34s %6d bytes' % (pg['slug'] + u'.html', len(html.encode('utf-8'))))
