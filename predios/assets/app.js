/* ========================================================
   LM PREDIOS — CONTROLADOR DE COMPONENTES INTERACTIVOS
   Reutiliza los componentes nativos de la web de LM:
   - Carrusel con navegación y snap scroll
   - Lightbox con zoom progresivo y arrastre pan
   - Visor de Partida Registral SUNARP
   - Enlace directo a WhatsApp
   ======================================================== */
(function () {
  "use strict";

  // Helper de selección
  const $ = (id) => document.getElementById(id);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  /* ========================================================
     1. CARRUSEL DE IMÁGENES REUTILIZADO
     ======================================================== */
  function initCarousel() {
    const carousels = $$("[data-carousel]");
    carousels.forEach((carousel) => {
      const track = carousel.querySelector("[data-carousel-track]");
      const prev = carousel.querySelector(".carousel-nav.prev");
      const next = carousel.querySelector(".carousel-nav.next");
      if (!track) return;

      const scrollBySlide = (dir) => {
        const slide = track.querySelector(".carousel-slide");
        if (!slide) return;
        const gap = 18;
        const step = slide.offsetWidth + gap;
        track.scrollBy({ left: dir * step, behavior: "smooth" });
      };

      if (prev) prev.addEventListener("click", () => scrollBySlide(-1));
      if (next) next.addEventListener("click", () => scrollBySlide(1));

      const updateButtons = () => {
        const maxScroll = track.scrollWidth - track.clientWidth - 4;
        if (prev) prev.disabled = track.scrollLeft <= 4;
        if (next) next.disabled = track.scrollLeft >= maxScroll;
      };

      track.addEventListener("scroll", updateButtons, { passive: true });
      window.addEventListener("resize", updateButtons, { passive: true });
      updateButtons();
    });
  }

  /* ========================================================
     2. LIGHTBOX / VISOR AMPLIADO (Componente del portafolio)
     ======================================================== */
  function initLightbox() {
    const lightbox = $("lightbox");
    if (!lightbox) return;

    const lbImg = $("lightboxImg");
    const lbCaptionText = $("lightboxCaptionText");
    const lbCaptionNum = $("lightboxCaptionNum");
    const lbCounter = $("lightboxCounter");
    const lbTotal = $("lightboxTotal");
    const lbClose = $("lightboxClose");
    const lbPrev = $("lightboxPrev");
    const lbNext = $("lightboxNext");
    const lbZoomIn = $("lightboxZoomIn");
    const lbZoomOut = $("lightboxZoomOut");
    const lbZoomReset = $("lightboxZoomReset");

    const items = $$("[data-lightbox]");
    if (lbTotal) lbTotal.textContent = items.length;

    if (items.length <= 1) {
      if (lbPrev) lbPrev.style.display = "none";
      if (lbNext) lbNext.style.display = "none";
      const counterDiv = lightbox.querySelector(".lightbox-counter");
      if (counterDiv) counterDiv.style.display = "none";
    }

    let currentIdx = 0;
    let zoom = 1;
    let panX = 0,
      panY = 0;

    function applyTransform() {
      if (!lbImg) return;
      lbImg.style.transform = `translate(${panX}px, ${panY}px) scale(${zoom})`;
      lbImg.classList.toggle("zoomed", zoom > 1);
    }

    function show(idx) {
      if (!items.length) return;
      currentIdx = (idx + items.length) % items.length;
      const el = items[currentIdx];
      if (lbImg) {
        lbImg.src = el.dataset.src || el.getAttribute("src") || "";
        lbImg.alt = el.dataset.caption || "Fotografía ampliada";
      }
      if (lbCaptionText) lbCaptionText.textContent = " " + (el.dataset.caption || "");
      if (lbCaptionNum) lbCaptionNum.textContent = el.dataset.num || "";
      if (lbCounter) lbCounter.textContent = currentIdx + 1;
      zoom = 1;
      panX = 0;
      panY = 0;
      applyTransform();
    }

    function open(idx) {
      show(idx);
      lightbox.classList.add("open");
      document.body.style.overflow = "hidden";
    }

    function close() {
      lightbox.classList.remove("open");
      document.body.style.overflow = "";
    }

    items.forEach((el, idx) => {
      el.addEventListener("click", () => open(idx));
    });

    if (lbClose) lbClose.addEventListener("click", close);
    if (lbPrev) lbPrev.addEventListener("click", () => show(currentIdx - 1));
    if (lbNext) lbNext.addEventListener("click", () => show(currentIdx + 1));

    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox || e.target.classList.contains("lightbox-stage")) {
        close();
      }
    });

    // Controles de zoom
    if (lbZoomIn) {
      lbZoomIn.addEventListener("click", () => {
        zoom = Math.min(zoom + 0.35, 4);
        applyTransform();
      });
    }
    if (lbZoomOut) {
      lbZoomOut.addEventListener("click", () => {
        zoom = Math.max(zoom - 0.35, 1);
        if (zoom === 1) {
          panX = 0;
          panY = 0;
        }
        applyTransform();
      });
    }
    if (lbZoomReset) {
      lbZoomReset.addEventListener("click", () => {
        zoom = 1;
        panX = 0;
        panY = 0;
        applyTransform();
      });
    }

    // Doble clic o clic en imagen para alternar zoom 1x <-> 2x
    if (lbImg) {
      lbImg.addEventListener("click", (e) => {
        e.stopPropagation();
        if (zoom > 1) {
          zoom = 1;
          panX = 0;
          panY = 0;
        } else {
          zoom = 2;
        }
        applyTransform();
      });

      // Pan con mouse
      let isDragging = false;
      let dragStartX = 0,
        dragStartY = 0;
      let panStartX = 0,
        panStartY = 0;

      lbImg.addEventListener("mousedown", (e) => {
        if (zoom <= 1) return;
        isDragging = true;
        lbImg.classList.add("dragging");
        dragStartX = e.clientX;
        dragStartY = e.clientY;
        panStartX = panX;
        panStartY = panY;
        e.preventDefault();
      });

      window.addEventListener("mousemove", (e) => {
        if (!isDragging) return;
        panX = panStartX + (e.clientX - dragStartX);
        panY = panStartY + (e.clientY - dragStartY);
        applyTransform();
      });

      window.addEventListener("mouseup", () => {
        isDragging = false;
        if (lbImg) lbImg.classList.remove("dragging");
      });

      // Pan táctil móvil
      let touchStartX = 0,
        touchStartY = 0;
      lbImg.addEventListener(
        "touchstart",
        (e) => {
          if (zoom <= 1 || e.touches.length !== 1) return;
          isDragging = true;
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
          panStartX = panX;
          panStartY = panY;
        },
        { passive: true }
      );

      lbImg.addEventListener(
        "touchmove",
        (e) => {
          if (!isDragging || e.touches.length !== 1) return;
          panX = panStartX + (e.touches[0].clientX - touchStartX);
          panY = panStartY + (e.touches[0].clientY - touchStartY);
          applyTransform();
          e.preventDefault();
        },
        { passive: false }
      );

      lbImg.addEventListener("touchend", () => {
        isDragging = false;
      });
    }

    // Zoom con rueda de mouse
    lightbox.addEventListener(
      "wheel",
      (e) => {
        if (!lightbox.classList.contains("open")) return;
        e.preventDefault();
        const delta = -Math.sign(e.deltaY) * 0.25;
        zoom = Math.max(1, Math.min(4, zoom + delta));
        if (zoom === 1) {
          panX = 0;
          panY = 0;
        }
        applyTransform();
      },
      { passive: false }
    );

    // Navegación por teclado
    document.addEventListener("keydown", (e) => {
      if (!lightbox.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(currentIdx - 1);
      if (e.key === "ArrowRight") show(currentIdx + 1);
      if (e.key === "+" || e.key === "=") {
        zoom = Math.min(zoom + 0.35, 4);
        applyTransform();
      }
      if (e.key === "-" || e.key === "_") {
        zoom = Math.max(zoom - 0.35, 1);
        if (zoom === 1) {
          panX = 0;
          panY = 0;
        }
        applyTransform();
      }
      if (e.key === "0") {
        zoom = 1;
        panX = 0;
        panY = 0;
        applyTransform();
      }
    });
  }

  /* ========================================================
     3. VISOR MODAL DE PARTIDA REGISTRAL
     ======================================================== */
  function initModalPartida() {
    const modal = $("modalPartida");
    const openBtns = $$("[data-open-partida]");
    const closeBtn = $("modalPartidaClose");

    if (!modal) return;

    function openModal() {
      modal.classList.add("open");
      document.body.style.overflow = "hidden";
    }

    function closeModal() {
      modal.classList.remove("open");
      document.body.style.overflow = "";
    }

    openBtns.forEach((btn) => btn.addEventListener("click", openModal));
    if (closeBtn) closeBtn.addEventListener("click", closeModal);

    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeModal();
    });

    document.addEventListener("keydown", (e) => {
      if (modal.classList.contains("open") && e.key === "Escape") {
        closeModal();
      }
    });
  }

  // Inicializar al cargar el DOM
  document.addEventListener("DOMContentLoaded", () => {
    initCarousel();
    initLightbox();
    initModalPartida();
  });
})();
