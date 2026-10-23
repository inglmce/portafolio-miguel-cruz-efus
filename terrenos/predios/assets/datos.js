/* Única fuente de datos. Agrega nuevos predios a este catálogo sin tocar index.html. */
window.LM_PREDIOS = Object.freeze([
  {
    id: "lambayeque-san-martin-mz-m-lote-2",
    url: "lambayeque-san-martin-lote-2.html",
    titulo: "Terreno urbano en San Martín de Porres",
    localidad: "Pueblo Joven San Martín de Porres",
    distrito: "Lambayeque",
    provincia: "Lambayeque",
    departamento: "Lambayeque",
    direccion: "Calle Juan Manuel Iturregui, Mz. M, lote 2",
    referencia: "A pocas cuadras del Parque San Martín y de la I.E. San Martín Primaria",
    area: 195.57,
    frente: 7.40,
    derecha: 27.30,
    izquierda: 27.20,
    fondo: 6.86,
    usoRegistral: "Vivienda",
    partida: "P10003686",
    fechaConsulta: "23/10/2026",
    estado: "En venta",
    precio: null, // OBLIGATORIO: indicar monto y moneda ANTES de publicar.
    moneda: "PEN", // PEN o USD. Nunca inventar monto.
    sinCargasSegunResumen: true,
    mapa: "assets/ubicacion-lote.webp",
    maps: "https://www.google.com/maps/search/?api=1&query=Juan+Manuel+Iturregui+Jose+Olaya+Lambayeque+Peru",
    fotos: [], // P.ej. ["assets/fachada-01.webp", "assets/fachada-02.webp"]
    whatsapp: "51926179993",
    publicado: false // Borrador. Cambiar tras revisión legal y completar material.
  }
]);
