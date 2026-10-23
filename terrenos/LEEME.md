# Ampliación modular «Predios» — borrador de integración

## Qué contiene

- `predios/index.html`: catálogo independiente y ampliable. No modifica el menú de tu portafolio.
- `predios/lambayeque-san-martin-lote-2.html`: primera ficha de venta; cada predio futuro tendría su propio HTML.
- `predios/assets/datos.js`: **fuente única** con precio, área, linderos, ubicación, fotos y WhatsApp. Los HTML muestran los datos sin duplicarlos manualmente.
- `predios/assets/app.js`: dibuja el catálogo, la ficha y prepara el mensaje de WhatsApp (sin backend ni bases de datos).
- `predios/assets/estilos.css`: estética compatible con tu web, totalmente aislada.
- `predios/assets/ubicacion-lote.webp`: imagen de ubicación proporcionada y optimizada.

## Integración en tu sitio

Copia **la carpeta `predios/`** en la raíz de tu sitio junto a `index.html`, `proyectos/` y `aplicaciones/`.

La URL pública proyectada es:
`https://luismiguelcruzefus.com/predios/lambayeque-san-martin-lote-2.html`

El portafolio principal no requiere ningún cambio. El nuevo módulo se encuentra fuera de su menú, pero cualquier persona puede abrirlo con el enlace directo.

## Antes de publicar

1. Definir el **precio real de venta** en `predios/assets/datos.js` (campo `precio`, número sin separadores de millares). La moneda se controla con `moneda` (`PEN` o `USD`). No se ha inventado ningún precio.
2. Añadir las fotos reales en `predios/assets/` (preferiblemente WebP), por ejemplo `fachada-01.webp`. Agregarlas al array `fotos` del registro: `fotos: ["assets/fachada-01.webp"]`. La galería aparece automáticamente; si hay más fotos se agregan a continuación sin editar HTML.
3. **Corregir un dato de la imagen**: el rótulo del diseño que dice «Distrito de Pueblo Joven San Martín de Porres» confunde localidad con distrito. La partida ubica el predio en el distrito de **Lambayeque**, provincia de Lambayeque, departamento de Lambayeque. La ficha HTML sí lo expresa correctamente. Sustituir la imagen tras corregir el texto.
4. Verificar **titularidad y autorización de venta**: el resumen adjunto consigna titulares registrales específicos. Si quien publicita no es titular, debe contar con autorización apropiada antes de ofrecer el bien y aclarar si existe intermediación inmobiliaria.
5. Validar servicios, parámetros, situación física, disponibilidad y documentos con fuentes actualizadas. No se han inventado zonificación, factibilidad ni permisos.
6. Cuando todo esté listo, cambiar `publicado: false` por `true` en `datos.js` y actualizar los metadatos `<meta name="robots" content="noindex,nofollow">` a `index,follow` **en ambas páginas**.

## Prueba local

Puedes abrir ambos HTML directamente en Chrome. Si deseas simular servidor, desde la carpeta que contiene `predios/`: `python -m http.server 8080` y luego abrir `http://localhost:8080/predios/`.

## Importante sobre registro

La hoja de resumen SUNARP del 23/10/2026 muestra partida activa y situación `NO CARG/GRAV`; también consigna hipoteca registrada en 2001, cancelada en 2003. La ficha evita afirmar más de lo que el documento permite. No se recomienda publicar el PDF completo con datos personales de terceros. Los compradores pueden realizar sus verificaciones registrales antes de comprometer pagos.

## Arquitectura para futuros predios

Al agregar un predio: añadir un objeto a `predios/assets/datos.js` y crear un HTML de detalle con el mismo esquema y un `data-id` único. El índice agrega automáticamente la tarjeta; no es necesario tocar ni añadir un enlace en la web principal. La capa de datos permite después reemplazar el array por API o CMS sin rediseñar el frontend.
