(function () {
  "use strict";
  const properties = window.LM_PREDIOS || [];
  const number = v => Number(v).toFixed(2);
  const $ = id => document.getElementById(id);
  const set = (id, value) => { if ($(id)) $(id).textContent = value; };
  const money = p => {
    if (p.precio === null || !Number.isFinite(p.precio)) return "Precio por definir";
    return new Intl.NumberFormat("es-PE", {style:"currency", currency:p.moneda || "PEN",maximumFractionDigits:0}).format(p.precio);
  };
  function listing() {
    const grid = $("catalogo");
    if (!grid) return;
    properties.forEach(p => {
      const a = document.createElement("a");
      a.className = "list-card";
      a.href = p.url;
      const photo = document.createElement("div");
      photo.className = "list-img";
      const img = document.createElement("img");
      img.src = (p.fotos[0] || p.mapa);
      img.loading = "lazy";
      img.alt = p.fotos.length ? "Fotografía del terreno" : "Plano de ubicación del terreno";
      photo.append(img);
      const body = document.createElement("div"); body.className="list-body";
      const state = document.createElement("span"); state.className="eyebrow"; state.textContent=p.estado;
      const title = document.createElement("h2"); title.textContent=p.titulo;
      const local = document.createElement("p");local.className="small";local.textContent=`${p.distrito}, ${p.departamento}`;
      const foot = document.createElement("div");foot.className="list-foot";
      const k = document.createElement("span");k.textContent="Ver ficha del predio";
      const arrow = document.createElement("span"); arrow.textContent="→";
      foot.append(k,arrow);body.append(state,title,local,foot);a.append(photo,body);grid.append(a);
    });
    set("n-predios",`${properties.length} ${properties.length===1?"predio":"predios"}`);
  }
  function detail() {
    const root = $("detalle"); if (!root) return;
    const p = properties.find(item=>item.id===root.dataset.id);
    if (!p) { set("titulo", "Predio no encontrado"); return; }
    set("titulo", p.titulo); set("localidad",`${p.localidad} · ${p.distrito}, ${p.departamento}`);
    set("estado",p.estado);set("precio",money(p));set("area", `${number(p.area)} m²`);
    set("frente",`${number(p.frente)} m`);set("fondo",`${number(p.fondo)} m`);
    set("direccion",p.direccion);set("derecha",`${number(p.derecha)} m`);
    set("izquierda",`${number(p.izquierda)} m`);set("uso",p.usoRegistral);
    set("partida",p.partida);set("fecha-consulta",p.fechaConsulta);
    set("estado-registro", p.sinCargasSegunResumen ? "Partida activa; sin cargas ni gravámenes según resumen consultado" : "Consultar la información registral");
    set("reference",p.referencia);
    const map = $("mapa-imagen"); if (map) map.src=p.mapa;
    const maps = $("google-maps"); if (maps) maps.href=p.maps;
    const gallery = $("galeria");
    if(gallery && p.fotos && p.fotos.length){
      gallery.classList.remove("hidden");
      const first = $("foto-principal"); if (first) {first.src=p.fotos[0];first.alt="Fotografía real de la fachada del terreno";}
      const extras = $("fotos-secundarias");
      p.fotos.slice(1).forEach((src,i)=>{
        const img=document.createElement("img");img.src=src;img.loading="lazy";img.alt=`Fotografía adicional del predio ${i+2}`;extras.append(img);
      });
      if(p.fotos.length===1) extras.classList.add("hidden");
    }
    if (p.publicado && Number.isFinite(p.precio)) $("borrador").classList.add("hidden");
    const form = $("consulta");
    if(form){
      form.addEventListener("submit", e=>{
        e.preventDefault();
        if(!form.reportValidity()) return;
        const nombre=$("nombre").value.trim();
        const compra=$("modalidad").value;
        const intencion=$("intencion").value;
        const msg=`Hola, mi nombre es ${nombre}. Revisé la ficha del terreno (Mz. M, lote 2, Lambayeque). Modalidad prevista: ${compra}. ${intencion}. Quisiera confirmar disponibilidad y coordinar los siguientes pasos.`;
        const link=`https://wa.me/${p.whatsapp}?text=${encodeURIComponent(msg)}`;
        window.open(link,"_blank","noopener,noreferrer");
      });
    }
  }
  listing();detail();
})();
