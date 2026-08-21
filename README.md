# Portafolio Profesional — Luis Miguel Cruz Efus

> Ingeniero Civil · Especialista BIM · Experto en Inteligencia Artificial
> CIP N.° 339195 · Lima, Perú
> Publicado en **https://luismiguelcruzefus.com**

---

## 📁 Estructura del sitio

```
PORTAFOLIO PROFESIONAL/
├── index.html                  ← Página principal (§01 Perfil … §05 Stack + Contacto)
├── proyectos/                  ← § 02 · Casos de éxito (4 fichas: PTAR/PTAP)
│   ├── ptar-tocache.html
│   ├── ptar-chota.html
│   ├── ptar-san-cristobal.html
│   └── ptap-tocache.html
├── aplicaciones/               ← § 03 · Ecosistema de aplicaciones (12 fichas)
│   ├── asistente-sismico.html
│   ├── copimetrados.html
│   └── … (una por app publicada en Microsoft Store)
├── ia/                         ← § 04 · IA & Automatización (4 fichas)
│   ├── lmbimtools.html
│   ├── servidores-mcp.html
│   ├── automatizacion-presupuestos.html
│   └── agentes-ia.html
├── imagenes/
│   ├── proyectos_bim/          ← renders y planos de cada PTAR/PTAP
│   └── lm_ingenieria/          ← carátulas de apps y de la sección IA
├── _herramientas/              ← scripts de mantenimiento (Jekyll NO los publica)
│   └── generar_fichas_ia.py    ← regenera las 4 fichas de ia/ desde su contenido
├── nebula-mesh.js
├── sitemap.xml · robots.txt · CNAME
└── README.md
```

**Numeración de secciones del index** — si insertas una sección nueva hay que recorrer las
siguientes: `§ 01` Perfil · `§ 02` Casos de éxito · `§ 03` Aplicaciones ·
`§ 04` IA & Automatización · `§ 05` Stack. Contacto usa coordenadas `N.06` / `N.07`.

---

## 🖼️ Carátulas de la sección IA & Automatización

Las 4 tarjetas de `§ 04` esperan su carátula vertical (9:16) en estas rutas exactas:

| Tarjeta | Ruta del archivo |
|---|---|
| LMBIMTools | `imagenes/lm_ingenieria/lmbimtools/00_caratula.png` |
| Servidores MCP | `imagenes/lm_ingenieria/servidores_mcp/00_caratula.png` |
| Automatización de presupuestos | `imagenes/lm_ingenieria/automatizacion_presupuestos/00_caratula.png` |
| Agentes de IA | `imagenes/lm_ingenieria/agentes_ia/00_caratula.png` |

Las carpetas ya existen y **el sitio funciona sin las imágenes**: mientras falten, cada tarjeta
muestra un rótulo tipográfico de reserva (`onerror`). Basta con dejar caer el PNG con ese nombre
para que aparezca la carátula, sin tocar el HTML.

---

## ➕ Cómo añadir un **nuevo proyecto** (caso de éxito)

1. Duplica una ficha existente, p. ej. `proyectos/ptar-chota.html`, y renómbrala.
2. Reemplaza dentro: `<title>`, la descripción `<meta>`, el `og:`/`twitter:`, el `<h1 class="display">`,
   los chips, la ficha técnica y los bloques de contenido.
3. Crea `imagenes/proyectos_bim/<nombre_del_proyecto>/` y pon ahí los renders y planos.
   **No uses servicios externos de imágenes:** todo el material vive en el repositorio.
4. En `index.html`, sección `<!-- ============ PROYECTOS ============ -->`, duplica una tarjeta `<a class="card">`
   y apunta su `href` y su `<img src>` al proyecto nuevo.
5. Añade la URL a `sitemap.xml`.

## ➕ Cómo añadir una **nueva aplicación**

Igual que arriba, pero sobre `aplicaciones/` y la sección `<!-- ============ APLICACIONES ============ -->`.
Recuerda actualizar el contador `12 publicados` de la cabecera de la sección y añadir el Store ID
a `enlaces_microsoft_store.md`.

## ✏️ Cómo editar las **fichas de IA & Automatización**

Las 4 páginas de `ia/` se generan desde un solo script para que no se desincronicen entre sí:

```bash
python "_herramientas/generar_fichas_ia.py"
```

El contenido (títulos, párrafos, features, listado de herramientas y cierre) está en la lista
`PAGINAS` del script; la plantilla común está arriba, en `CABECERA`. Edita ahí y vuelve a ejecutar
— sobrescribe las cuatro páginas. Si prefieres tocar el HTML a mano, hazlo, pero entonces no
vuelvas a ejecutar el script o perderás el cambio.

---

## 🎨 Sistema visual (para mantener consistencia)

- **Acento ámbar:** `oklch(0.78 0.14 65)` — solo para énfasis, nunca para fondos grandes.
- **Acento azul:** `oklch(0.72 0.10 245)` — segundo plano de jerarquía (CTA pareado del hero).
- **Fondo principal:** `oklch(0.16 0.012 250)` (variable `--ink`).
- **Tipografías:**
  - Display editorial: `Instrument Serif` (cursiva para el énfasis)
  - Cuerpo: `Geist`
  - Etiquetas técnicas: `JetBrains Mono`
- **Lenguaje único:** coordenadas tipo `N.01`, líneas de acotación, esquinas con corchetes,
  rejilla *blueprint* de fondo y carátulas verticales 9:16.

Cualquier sección nueva debe respetar estos elementos para que se sienta parte del mismo
"cuaderno técnico".

---

## 🔍 Cómo previsualizar en local

```bash
python -m http.server 8760 --directory "PORTAFOLIO PROFESIONAL"
```

Luego abrir `http://localhost:8760`. Está también registrado como configuración `portafolio`
en `.claude/launch.json` del espacio de trabajo.

---

## 🚀 Publicación

El sitio se sirve por GitHub Pages desde la rama `main` en la raíz, con dominio propio declarado
en `CNAME` (`luismiguelcruzefus.com`). Al añadir páginas hay que actualizar `sitemap.xml`.
Las rutas y nombres de archivo son **sensibles a mayúsculas** en el servidor: `logo.png` no es
`LOGO.png`, aunque en Windows parezcan lo mismo.

---

## 📌 Pendientes

- [x] Las 4 carátulas de `§ 04 IA & Automatización` ya están colocadas (941 × 1672 px, como el resto).
      Originales en `02_REDES SOCIALES Y CONTENIDO/{LM_BIM_Tools,MCP,Presupuestos,Agentes_AI}/`.
- [ ] **Regenerar la carátula de Agentes de IA**: la actual anuncia «agente secundario que vigila
      mercados», «histórico y cambios» y «alertas automáticas WhatsApp / correo». El agente del SEACE
      no tiene ninguna de esas tres cosas y el texto del sitio ya no las menciona.
- [x] Correo de contacto confirmado: **`miguelefus@gmail.com`** es el único funcional. No debe
      aparecer ningún otro en el sitio.
- [x] Redes sociales: solo WhatsApp, LinkedIn y YouTube (más GitHub en el `sameAs` del JSON-LD).
      **Sin Facebook ni Instagram** — no volver a añadirlos.
- [ ] Revisar si CopiSanitario debe anunciarse con 13 o 14 módulos (el módulo 00 se cuenta aparte).
- [ ] Restituir o retirar definitivamente `privacidad.html` (se eliminó del sitio; ya salió del sitemap).
- [ ] Sumar nuevos casos de éxito a medida que se cierren expedientes.

---

© 2026 · Luis Miguel Cruz Efus
