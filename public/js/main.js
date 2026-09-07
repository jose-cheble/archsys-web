(function () {
  const WHATSAPP_NUMBER = "5493516644041";
  const SUPPORT_EMAIL = "soporte@archsys.com.ar";

  const headerNav = document.querySelector(".nav");
  const menuToggle = document.querySelector(".menu-toggle");
  const yearEl = document.getElementById("year");
  const form = document.getElementById("contact-form");
  const statusEl = document.getElementById("form-status");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  if (menuToggle && headerNav) {
    menuToggle.addEventListener("click", function () {
      headerNav.classList.toggle("is-open");
    });

    headerNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        headerNav.classList.remove("is-open");
      });
    });
  }

  function fieldValue(id) {
    const el = document.getElementById(id);
    return el ? el.value.trim() : "";
  }

  function buildMessage() {
    const nombre = fieldValue("nombre");
    const empresa = fieldValue("empresa");
    const email = fieldValue("email");
    const telefono = fieldValue("telefono");
    const motivo = fieldValue("motivo");
    const mensaje = fieldValue("mensaje");

    return [
      "Consulta desde archsys.com.ar",
      "",
      "Nombre: " + nombre,
      "Empresa: " + (empresa || "\u2014"),
      "Email: " + email,
      "Tel\u00e9fono: " + (telefono || "\u2014"),
      "Motivo: " + motivo,
      "",
      mensaje
    ].join("\n");
  }

  function showStatus(message, ok) {
    if (!statusEl) return;
    statusEl.textContent = message;
    statusEl.className = "form-status " + (ok ? "is-ok" : "is-error");
  }

  function validateForm() {
    const nombre = fieldValue("nombre");
    const email = fieldValue("email");
    const mensaje = fieldValue("mensaje");

    if (!nombre || !email || !mensaje) {
      showStatus("Complet\u00e1 nombre, email y mensaje para continuar.", false);
      return false;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      showStatus("Ingres\u00e1 un email v\u00e1lido.", false);
      return false;
    }

    return true;
  }

  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
    });

    document.getElementById("send-whatsapp").addEventListener("click", function () {
      if (!validateForm()) return;
      const text = encodeURIComponent(buildMessage());
      window.open("https://wa.me/" + WHATSAPP_NUMBER + "?text=" + text, "_blank", "noopener");
      showStatus("Se abri\u00f3 WhatsApp con tu consulta. Envi\u00e1 el mensaje para completar el contacto.", true);
    });

    document.getElementById("send-email").addEventListener("click", function () {
      if (!validateForm()) return;
      const subject = encodeURIComponent("Consulta \u2014 Arch Sistemas");
      const body = encodeURIComponent(buildMessage());
      window.location.href = "mailto:" + SUPPORT_EMAIL + "?subject=" + subject + "&body=" + body;
      showStatus("Se abri\u00f3 tu cliente de email. Envi\u00e1 el correo para completar el contacto.", true);
    });
  }

  document.querySelectorAll("[data-lightbox]").forEach(function (img) {
    img.addEventListener("click", function () {
      if (!lightbox || !lightboxImg) return;
      lightboxImg.src = img.getAttribute("src");
      lightboxImg.alt = img.getAttribute("alt") || "Captura de pantalla";
      lightbox.classList.add("is-open");
    });
  });

  if (lightbox) {
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox || event.target.classList.contains("lightbox-close")) {
        lightbox.classList.remove("is-open");
        lightboxImg.src = "";
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        lightbox.classList.remove("is-open");
      }
    });
  }
})();
