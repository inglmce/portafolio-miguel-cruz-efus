# Portafolio Profesional — Luis Miguel Cruz Efus

> Ingeniero Civil · Especialista BIM · Desarrollador
> CIP N.° 339195 · Lima, Perú

## 📁 Estructura del proyecto

```
portafolio/
├── index.html                          ← Página principal (la que abre el reclutador)
├── proyectos/
│   └── ptar-tocache.html              ← Caso de estudio Tocache
├── aplicativos/
│   └── asistente-sismico.html         ← Ejemplo de detalle de aplicativo
└── README.md                           ← Esta guía
```

## 🚀 Cómo subirlo a GitHub Pages

1. Crea un repositorio nuevo en GitHub llamado `portafolio` (o el nombre que prefieras).
2. Sube los tres archivos respetando las carpetas `proyectos/` y `aplicativos/`.
3. En el repositorio, ve a **Settings → Pages**.
4. En **Source**, selecciona **Deploy from a branch → main → / (root)** y guarda.
5. Espera 1–2 minutos. Tu portafolio quedará en:
   `https://TU-USUARIO.github.io/portafolio/`

Copia ese enlace en tu CV.

---

## ➕ Cómo añadir un **nuevo proyecto** (por ejemplo PTAR Chota)

### Paso 1 — Duplica el archivo de Tocache
Copia `proyectos/ptar-tocache.html` y renómbralo, por ejemplo `proyectos/ptar-chota.html`.

### Paso 2 — Edita el contenido
Abre el nuevo archivo y reemplaza:
- **Título** de la página (`<title>` y el `<h1 class="display">`)
- **Chips** (sector, año, rol)
- **Ficha técnica** (rol, cliente, periodo, stack)
- **Problema · Solución · Resultado** — los tres bloques `<div class="step-card">`
- **Imágenes** — sube tus capturas a [postimg.cc](https://postimg.cc) (gratis, sin cuenta) y pega los enlaces directos en `<img src="...">`.

### Paso 3 — Actívalo en el index
Abre `index.html`. Busca la sección `<!-- ============ PROYECTOS ============ -->`. Las dos tarjetas "En documentación" tienen este patrón:

```html
<div class="card p-8 lg:p-10">
  <div class="cover placeholder ...">
    ...
  </div>
  ...
</div>
```

Para convertir una tarjeta "en documentación" en proyecto real:
1. Cambia `<div class="card ...">` por `<a href="proyectos/ptar-chota.html" class="card ...">` (y cierra con `</a>`).
2. Quita la clase `placeholder` y `empty-pulse` del `.cover`.
3. Reemplaza el contenido interno por una `<img src="URL_DE_TU_PORTADA" alt="...">`.
4. Quita el chip "Próximamente".

---

## 📱 Cómo añadir un **nuevo aplicativo**

### Paso 1 — Duplica la plantilla
Copia `aplicativos/asistente-sismico.html` y renómbralo, por ejemplo `aplicativos/vigas-concreto-armado.html`.

### Paso 2 — Edita
Reemplaza:
- Título, h1, chips, ficha técnica
- Bloques `<div class="feature">` con las características que automatiza
- Las cuatro tarjetas placeholder de la sección "Capturas del aplicativo" — sube tus screenshots a postimg.cc y reemplaza los `<div class="img-frame placeholder">` por `<div class="img-frame"><img src="..."></div>`
- Notas de desarrollo

### Paso 3 — Activa el link en el index
Abre `index.html`, sección `<!-- ============ APLICATIVOS ============ -->`. Cada tarjeta de aplicativo tiene el patrón:

```html
<div class="card group" data-reveal>
  ...
</div>
```

Para hacerla cliqueable:
1. Cambia `<div class="card group" ...>` por `<a href="aplicativos/vigas-concreto-armado.html" class="card group" ...>` (y el cierre `</div>` por `</a>`).
2. Cambia el texto del pie de tarjeta de `Documentación en preparación` a `Ver demo →` con color de acento (mira cómo está hecho el Asistente Sísmico).

---

## 🎨 Sistema visual (para mantener consistencia)

- **Color de acento (ámbar):** `oklch(0.78 0.14 65)` — úsalo solo para énfasis, nunca para fondos grandes.
- **Fondo principal:** `oklch(0.16 0.012 250)` (variable `--ink`).
- **Tipografías:**
  - Display editorial: `Instrument Serif` (italic para énfasis)
  - Cuerpo: `Geist`
  - Etiquetas técnicas: `JetBrains Mono`
- **Lenguaje único:** etiquetas tipo `N.01`, líneas de acotación, esquinas con corchetes.

Cualquier sección nueva debería respetar estos elementos para que se sienta parte del mismo "cuaderno técnico".

---

## 🛠️ Edición rápida sin saber código

Si te incomoda HTML, lo más cómodo es:
1. Abrir el archivo en **VS Code** (gratis).
2. Buscar el texto que quieres cambiar (Ctrl+F).
3. Reemplazarlo. Las imágenes son siempre `<img src="URL">` — solo cambia la URL.

---

## 📌 Pendientes recomendados (siguientes pasos)

- [x] Configurar URL real de LinkedIn (`https://www.linkedin.com/in/luis-miguel-cruz-efus-6968b6154/`).
- [ ] Confirmar tu correo en la sección Contacto (actualmente `lmcruzef@gmail.com`).
- [ ] Subir las capturas reales del Asistente Sísmico para reemplazar los placeholders.
- [ ] Sumar PTAR Chota y un proyecto rural en los próximos meses.
- [ ] Convertir las tarjetas de aplicativos restantes en cliqueables a medida que documentes cada uno.

---

© 2026 · Luis Miguel Cruz Efus
