# ASCII-only generator. Writes site files as UTF-8.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def out(rel, text, newline="\n"):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.replace("\r\n", "\n").replace("\r", "\n")
    if newline == "\n" and not data.endswith("\n"):
        data += "\n"
    path.write_text(data, encoding="utf-8", newline=newline)
    print("wrote", path)


index = """<!DOCTYPE html>
<html lang="es-AR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Arch Sistemas | Gesti\u00f3n integral de ascensores</title>
  <meta name="description" content="Software profesional para la gesti\u00f3n de ascensores: inspecciones, edificios, equipos, monitoreo de rutas, reportes y c\u00f3digos QR. Arch Sistemas, C\u00f3rdoba Capital, Argentina.">
  <meta name="theme-color" content="#10385e">
  <link rel="canonical" href="https://archsys.com.ar/">
  <link rel="icon" href="./favicon.ico" type="image/x-icon">
  <meta property="og:title" content="Arch Sistemas | Gesti\u00f3n integral de ascensores">
  <meta property="og:description" content="Plataforma empresarial para conservar, inspeccionar y reportar el parque de ascensores.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://archsys.com.ar/">
  <meta property="og:image" content="https://archsys.com.ar/assets/brand/arch-logo.png">
  <meta property="og:locale" content="es_AR">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./css/styles.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Arch Sistemas",
    "url": "https://archsys.com.ar",
    "email": "soporte@archsys.com.ar",
    "telephone": "+5493516644041",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "C\u00f3rdoba Capital",
      "addressRegion": "C\u00f3rdoba",
      "addressCountry": "AR"
    },
    "description": "Software profesional para la gesti\u00f3n integral de ascensores."
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="#inicio" aria-label="Arch Sistemas">
        <img src="./assets/brand/arch-logo.png" alt="Arch Sistemas">
      </a>
      <button class="menu-toggle" type="button" aria-label="Abrir men\u00fa">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav" aria-label="Principal">
        <a href="#producto">Producto</a>
        <a href="#funcionalidades">Funcionalidades</a>
        <a href="#operacion">Operaci\u00f3n</a>
        <a href="#contacto">Contacto</a>
        <a class="nav-cta" href="#contacto">Solicitar informaci\u00f3n</a>
      </nav>
    </div>
  </header>

  <main id="inicio">
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <p class="section-kicker" style="color: rgba(255,255,255,.72)">Software para empresas de ascensores</p>
          <h1>Gesti\u00f3n integral de ascensores</h1>
          <p>
            Arch Sistemas centraliza inspecciones, reclamos, edificios, equipos y reportes
            en una plataforma seria, pensada para conservadores, administraciones y equipos t\u00e9cnicos.
          </p>
          <div class="hero-actions">
            <a class="btn btn-light" href="#contacto">Hablar con soporte</a>
            <a class="btn btn-outline" href="#funcionalidades">Ver funcionalidades</a>
          </div>
          <div class="hero-meta">
            <span>C\u00f3rdoba Capital, Argentina</span>
            <span>soporte@archsys.com.ar</span>
            <span>+54 9 351 664-4041</span>
          </div>
        </div>
        <div>
          <figure class="hero-frame">
            <img src="./assets/screenshots/inspecciones.svg" alt="Vista de inspecciones del sistema Arch" data-lightbox>
            <figcaption class="placeholder-note">Imagen ilustrativa. Reemplazar por captura real en assets/screenshots/inspecciones.svg</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="trust-bar">
      <div class="container trust-inner">
        <div class="trust-item">
          <strong>Operaci\u00f3n diaria</strong>
          <span>Inspecciones, reclamos y pruebas de seguridad en un mismo tablero.</span>
        </div>
        <div class="trust-item">
          <strong>Trabajo en campo</strong>
          <span>Escaneo QR desde el celular del t\u00e9cnico, sin papeles.</span>
        </div>
        <div class="trust-item">
          <strong>Control de flota</strong>
          <span>Edificios, equipos, conservadores y administraciones.</span>
        </div>
        <div class="trust-item">
          <strong>Evidencia formal</strong>
          <span>Reportes PDF, estad\u00edsticas y trazabilidad por usuario.</span>
        </div>
      </div>
    </section>

    <section class="section" id="producto">
      <div class="container producto-grid">
        <div>
          <p class="section-kicker">El producto</p>
          <h2 class="section-title">Una plataforma para conservar y documentar el parque de ascensores</h2>
          <p class="section-lead">
            Arch naci\u00f3 para empresas que necesitan orden operativo: saber qu\u00e9 se visit\u00f3,
            qui\u00e9n lo hizo, en qu\u00e9 equipo y con qu\u00e9 resultado. El sistema cubre oficina y calle,
            con roles diferenciados y un registro \u00fanico de cada intervenci\u00f3n.
          </p>
          <p>
            Desde el escritorio se administran edificios, equipos, usuarios y normativa.
            En el edificio, el t\u00e9cnico identifica el ascensor con un c\u00f3digo QR e informa
            inspecci\u00f3n t\u00e9cnica, reclamo, inspecci\u00f3n RT o prueba de seguridad.
          </p>
          <div class="chip-row">
            <span class="chip chip-it">Inspecci\u00f3n t\u00e9cnica</span>
            <span class="chip chip-rt">Reclamo t\u00e9cnico</span>
            <span class="chip chip-irr">Inspecci\u00f3n RT</span>
            <span class="chip chip-ps">Prueba de seguridad</span>
          </div>
        </div>
        <figure>
          <img class="shot" src="./assets/screenshots/equipos.svg" alt="Ficha de equipo con c\u00f3digo QR" data-lightbox>
          <figcaption class="shot-caption">Imagen ilustrativa. Reemplazar por captura real: equipos.svg</figcaption>
        </figure>
      </div>
    </section>

    <section class="section features" id="funcionalidades">
      <div class="container">
        <p class="section-kicker">Funcionalidades</p>
        <h2 class="section-title">Todo el circuito, de la visita al reporte</h2>
        <p class="section-lead">
          Cada m\u00f3dulo est\u00e1 pensado para el trabajo real de una empresa de ascensores:
          carga masiva, control de rutas, insumos y documentaci\u00f3n normativa.
        </p>

        <div class="feature-list">
          <article class="feature">
            <div>
              <h3>Inspecciones y reclamos en tiempo real</h3>
              <p>
                El inicio del sistema muestra las \u00faltimas intervenciones, con b\u00fasqueda,
                filtro por el d\u00eda y chips por tipo. Cada tarjeta identifica edificio,
                ciudad, equipo, observaci\u00f3n, direcci\u00f3n y t\u00e9cnico responsable.
              </p>
              <ul>
                <li>Inspecci\u00f3n t\u00e9cnica peri\u00f3dica</li>
                <li>Reclamo t\u00e9cnico con seguimiento</li>
                <li>Inspecci\u00f3n de responsable t\u00e9cnico</li>
                <li>Prueba de seguridad documentada</li>
              </ul>
            </div>
            <figure class="feature-media">
              <img src="./assets/screenshots/inspecciones.svg" alt="Listado de inspecciones" data-lightbox>
              <figcaption class="shot-caption">Reemplazar: assets/screenshots/inspecciones.svg</figcaption>
            </figure>
          </article>

          <article class="feature">
            <div>
              <h3>Edificios, equipos y padrones</h3>
              <p>
                El padr\u00f3n de edificios incluye direcci\u00f3n, barrio, ciudad, cantidad de equipos
                y estado de servicio. Desde cada ficha se accede al detalle del ascensor:
                marca, paradas, conservador, administraci\u00f3n e historial.
              </p>
              <ul>
                <li>Alta individual o carga masiva por planilla</li>
                <li>Servicio activo / inactivo con totales</li>
                <li>Ficha t\u00e9cnica completa de cada equipo</li>
              </ul>
            </div>
            <figure class="feature-media">
              <img src="./assets/screenshots/edificios.svg" alt="Tabla de edificios" data-lightbox>
              <figcaption class="shot-caption">Reemplazar: assets/screenshots/edificios.svg</figcaption>
            </figure>
          </article>

          <article class="feature">
            <div>
              <h3>Identificaci\u00f3n QR y trabajo m\u00f3vil</h3>
              <p>
                Cada equipo tiene un c\u00f3digo QR imprimible. El t\u00e9cnico abre el lector desde
                el celular, escanea en sitio o desde una foto, y registra la visita sobre
                el ascensor correcto. Se evitan errores de carga y planillas sueltas.
              </p>
              <ul>
                <li>Etiquetas con logo y datos del equipo</li>
                <li>Impresi\u00f3n masiva y regeneraci\u00f3n de c\u00f3digos</li>
                <li>Linterna y captura desde c\u00e1mara</li>
              </ul>
            </div>
            <figure class="feature-media">
              <img class="shot-mobile" src="./assets/screenshots/qr-movil.svg" alt="Esc\u00e1ner QR en celular" data-lightbox>
              <figcaption class="shot-caption">Reemplazar: assets/screenshots/qr-movil.svg</figcaption>
            </figure>
          </article>

          <article class="feature">
            <div>
              <h3>Monitoreo de rutas e insumos</h3>
              <p>
                Supervisi\u00f3n de la jornada: fecha, t\u00e9cnico, recorrido en mapa y paradas
                seg\u00fan el tipo de intervenci\u00f3n. Tambi\u00e9n se controla el consumo de insumos
                asociado a las visitas.
              </p>
              <ul>
                <li>Rutas diarias por t\u00e9cnico</li>
                <li>Monitoreo de inspecciones</li>
                <li>Seguimiento de insumos en campo</li>
              </ul>
            </div>
            <figure class="feature-media">
              <img src="./assets/screenshots/monitoreo.svg" alt="Mapa de monitoreo de rutas" data-lightbox>
              <figcaption class="shot-caption">Reemplazar: assets/screenshots/monitoreo.svg</figcaption>
            </figure>
          </article>

          <article class="feature">
            <div>
              <h3>Reportes y estad\u00edsticas</h3>
              <p>
                Indicadores mensuales y anuales, reportes por edificio, por administraci\u00f3n
                y por usuario. La evidencia queda lista para entregar a consorcios,
                auditor\u00edas internas o el responsable t\u00e9cnico.
              </p>
              <ul>
                <li>Generaci\u00f3n de reportes en PDF</li>
                <li>Estad\u00edsticas por edificio y por t\u00e9cnico</li>
                <li>Visi\u00f3n anual del cumplimiento</li>
              </ul>
            </div>
            <figure class="feature-media">
              <img src="./assets/screenshots/reportes.svg" alt="Tablero de estad\u00edsticas y reportes" data-lightbox>
              <figcaption class="shot-caption">Reemplazar: assets/screenshots/reportes.svg</figcaption>
            </figure>
          </article>

          <article class="feature">
            <div>
              <h3>Acciones masivas</h3>
              <p>
                Para empresas con un parque grande: importar edificios y equipos,
                asignar responsables en lote, regenerar QR e imprimir etiquetas
                con orden de impresi\u00f3n y vista previa.
              </p>
              <ul>
                <li>Carga masiva de edificios y equipos</li>
                <li>Asignaci\u00f3n masiva de edificios</li>
                <li>Impresi\u00f3n y regeneraci\u00f3n de QR</li>
              </ul>
            </div>
            <figure class="feature-media">
              <img src="./assets/screenshots/acciones-masivas.svg" alt="M\u00f3dulo de acciones masivas" data-lightbox>
              <figcaption class="shot-caption">Reemplazar: assets/screenshots/acciones-masivas.svg</figcaption>
            </figure>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="operacion">
      <div class="container">
        <p class="section-kicker">Qui\u00e9nes lo usan</p>
        <h2 class="section-title">Roles claros, la misma informaci\u00f3n</h2>
        <p class="section-lead">
          El acceso se define por tipo de usuario. Oficina, calle y supervisi\u00f3n
          trabajan sobre el mismo padr\u00f3n, sin planillas paralelas.
        </p>
        <div class="roles">
          <article class="role-card">
            <h3>Equipos t\u00e9cnicos</h3>
            <p>Registran visitas desde el celular, consultan el historial del equipo y cargan observaciones en el momento.</p>
          </article>
          <article class="role-card">
            <h3>Conservadores</h3>
            <p>Administran el parque a cargo, controlan cumplimiento y tienen trazabilidad de cada intervenci\u00f3n.</p>
          </article>
          <article class="role-card">
            <h3>Administraciones</h3>
            <p>Consultan el estado de los edificios que gestionan y reciben reportes formales cuando los necesitan.</p>
          </article>
        </div>

        <h2 class="section-title" style="margin-top: 64px">Tambi\u00e9n incluye</h2>
        <div class="more-grid">
          <article class="more-card">
            <h3>Usuarios y permisos</h3>
            <p>Altas, perfiles y control de qui\u00e9n ve o edita cada m\u00f3dulo. El t\u00e9cnico solo opera lo que le corresponde.</p>
          </article>
          <article class="more-card">
            <h3>Administraciones y conservadores</h3>
            <p>Padrones vinculados a edificios y equipos, con datos de contacto y asignaci\u00f3n.</p>
          </article>
          <article class="more-card">
            <h3>Normativa y mantenimiento</h3>
            <p>Configuraci\u00f3n de tareas, insumos y criterios normativos seg\u00fan la operaci\u00f3n de la empresa.</p>
          </article>
          <article class="more-card">
            <h3>Ciudades y barrios</h3>
            <p>Cat\u00e1logo geogr\u00e1fico para ubicar edificios y filtrar la operaci\u00f3n por zona.</p>
          </article>
          <article class="more-card">
            <h3>Manuales de uso</h3>
            <p>Gu\u00edas internas para uso general, edificios y equipos, y generaci\u00f3n de reportes.</p>
          </article>
          <article class="more-card">
            <h3>Soporte local</h3>
            <p>Desarrollado y acompa\u00f1ado desde C\u00f3rdoba Capital. Canal directo por WhatsApp o email.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section contacto" id="contacto">
      <div class="container">
        <p class="section-kicker">Contacto</p>
        <h2 class="section-title">Hablemos de su operaci\u00f3n</h2>
        <p class="section-lead">
          Escribinos por WhatsApp o email. Respondemos desde C\u00f3rdoba Capital.
        </p>
        <div class="contacto-grid">
          <aside class="contact-card">
            <h3 class="section-title" style="font-size: 1.35rem">Arch Sistemas</h3>
            <p>Software de gesti\u00f3n de ascensores. Atenci\u00f3n comercial y soporte t\u00e9cnico.</p>
            <div class="contact-list">
              <div>
                <strong>Tel\u00e9fono / WhatsApp</strong>
                <a href="https://wa.me/5493516644041" target="_blank" rel="noopener">+54 9 351 664-4041</a>
              </div>
              <div>
                <strong>Email</strong>
                <a href="mailto:soporte@archsys.com.ar">soporte@archsys.com.ar</a>
              </div>
              <div>
                <strong>Sede</strong>
                <p>C\u00f3rdoba Capital, Argentina</p>
              </div>
              <div>
                <strong>Sitio</strong>
                <p>archsys.com.ar</p>
              </div>
            </div>
          </aside>

          <form class="contact-form" id="contact-form" novalidate>
            <div class="form-grid">
              <div class="field">
                <label for="nombre">Nombre y apellido</label>
                <input id="nombre" name="nombre" type="text" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="empresa">Empresa</label>
                <input id="empresa" name="empresa" type="text" autocomplete="organization">
              </div>
              <div class="field">
                <label for="email">Email</label>
                <input id="email" name="email" type="email" autocomplete="email" required>
              </div>
              <div class="field">
                <label for="telefono">Tel\u00e9fono</label>
                <input id="telefono" name="telefono" type="tel" autocomplete="tel">
              </div>
              <div class="field full">
                <label for="motivo">Motivo</label>
                <select id="motivo" name="motivo">
                  <option>Quiero informaci\u00f3n del producto</option>
                  <option>Solicitar una demostraci\u00f3n</option>
                  <option>Soporte t\u00e9cnico</option>
                  <option>Otro</option>
                </select>
              </div>
              <div class="field full">
                <label for="mensaje">Mensaje</label>
                <textarea id="mensaje" name="mensaje" rows="5" required placeholder="Contanos cantidad de edificios, equipos o el motivo de la consulta."></textarea>
              </div>
            </div>
            <div class="form-actions">
              <button class="btn btn-whatsapp" id="send-whatsapp" type="button">Enviar por WhatsApp</button>
              <button class="btn btn-email" id="send-email" type="button">Enviar por email</button>
            </div>
            <p class="form-note">
              El formulario abre WhatsApp o tu cliente de correo con el mensaje ya armado.
              No almacenamos los datos en este sitio.
            </p>
            <div id="form-status" class="form-status" role="status"></div>
          </form>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <a class="footer-brand" href="#inicio">
        <img src="./assets/brand/arch-logo-transparente.png" alt="Arch Sistemas">
      </a>
      <p class="footer-copy">Arch \u00a9 <span id="year"></span> \u00b7 C\u00f3rdoba Capital, Argentina \u00b7 soporte@archsys.com.ar</p>
    </div>
  </footer>

  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Captura ampliada">
    <button class="lightbox-close" type="button" aria-label="Cerrar">\u00d7</button>
    <img id="lightbox-img" alt="">
  </div>

  <script src="./js/main.js"></script>
</body>
</html>
"""

js = """(function () {
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
      "Empresa: " + (empresa || "\\u2014"),
      "Email: " + email,
      "Tel\\u00e9fono: " + (telefono || "\\u2014"),
      "Motivo: " + motivo,
      "",
      mensaje
    ].join("\\n");
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
      showStatus("Complet\\u00e1 nombre, email y mensaje para continuar.", false);
      return false;
    }

    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {
      showStatus("Ingres\\u00e1 un email v\\u00e1lido.", false);
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
      showStatus("Se abri\\u00f3 WhatsApp con tu consulta. Envi\\u00e1 el mensaje para completar el contacto.", true);
    });

    document.getElementById("send-email").addEventListener("click", function () {
      if (!validateForm()) return;
      const subject = encodeURIComponent("Consulta \\u2014 Arch Sistemas");
      const body = encodeURIComponent(buildMessage());
      window.location.href = "mailto:" + SUPPORT_EMAIL + "?subject=" + subject + "&body=" + body;
      showStatus("Se abri\\u00f3 tu cliente de email. Envi\\u00e1 el correo para completar el contacto.", true);
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
"""

# The JS string above has double-escaped unicode because it lives inside a Python
# string that we want to emit as real JS unicode escapes. Decode them for the file.
js = js.encode("utf-8").decode("unicode_escape") if False else js
# Keep JS with real unicode via a second pass:
js = (
    js.replace("Complet\\\\u00e1", "Complet\u00e1")
    .replace("Ingres\\\\u00e1", "Ingres\u00e1")
    .replace("v\\\\u00e1lido", "v\u00e1lido")
    .replace("abri\\\\u00f3", "abri\u00f3")
    .replace("Envi\\\\u00e1", "Envi\u00e1")
    .replace("Tel\\\\u00e9fono", "Tel\u00e9fono")
    .replace("\\\\u2014", "\u2014")
    .replace("Consulta \\\\u2014", "Consulta \u2014")
)

readme = """# Arch Sistemas \u2014 sitio web

Landing institucional de **Arch Sistemas** para [archsys.com.ar](https://archsys.com.ar).
Presenta el producto de gesti\u00f3n de ascensores. Sitio est\u00e1tico, listo para Ubuntu o Debian en AWS.

## Contenido

```
public/                 Sitio que se publica
  index.html
  css/  js/
  assets/brand/         Logos oficiales del producto
  assets/screenshots/   Capturas ilustrativas (reemplazar)
deploy/
  setup-ubuntu.sh       Nginx + paquetes
  setup-ssl.sh          Certbot + cron de renovacion
  deploy.sh             Actualiza archivos en /var/www
  nginx-archsys.com.ar.conf
  certbot-renew.cron
```

## Vista local

Desde esta carpeta:

```bash
python3 -m http.server 8080 --directory public
```

Abrir `http://localhost:8080`.

En Windows (PowerShell):

```powershell
python -m http.server 8080 --directory public
```

## Capturas de pantalla

Las imagenes en `public/assets/screenshots/` son mockups.
Cuando tengas capturas reales, reemplazalas siguiendo `public/assets/screenshots/REEMPLAZAR.md`.

## Publicar en AWS (Ubuntu o Debian)

1. Apuntar el DNS de `archsys.com.ar` y `www.archsys.com.ar` a la IP publica de la instancia.
2. En el security group, abrir **80** y **443**.
3. Subir este repositorio al servidor.
4. Instalar el sitio:

```bash
sudo bash deploy/setup-ubuntu.sh
```

5. Emitir HTTPS y dejar el cron de renovacion:

```bash
sudo bash deploy/setup-ssl.sh
```

El cron queda en `/etc/cron.d/archsys-certbot` y corre todos los dias a las 03:17:

```
certbot renew --quiet --deploy-hook "systemctl reload nginx"
```

Certbot solo renueva si el certificado vence en menos de 30 dias. Despues de recargar Nginx el sitio sigue sirviendo el certificado nuevo.

Para actualizar el HTML o las imagenes:

```bash
sudo bash deploy/deploy.sh
```

## Contacto publicado

- Telefono / WhatsApp: +54 9 351 664-4041
- Email: soporte@archsys.com.ar
- Sede: Cordoba Capital, Argentina

El formulario no guarda datos en el servidor: abre WhatsApp o el cliente de correo del visitante con el mensaje ya armado.
"""

reemplazar = """# Como reemplazar las capturas ilustrativas

Los archivos de esta carpeta son mockups. Cuando tengas capturas reales del sistema, reemplaza cada archivo **manteniendo el mismo nombre**.

| Archivo | Pantalla |
|---|---|
| `inspecciones.svg` | Inicio / listado de inspecciones |
| `edificios.svg` | Tabla de edificios |
| `equipos.svg` | Detalle de equipo + QR |
| `qr-movil.svg` | Escaner QR en celular |
| `monitoreo.svg` | Monitoreo de rutas |
| `reportes.svg` | Estadisticas y reportes |
| `acciones-masivas.svg` | Acciones masivas |

Si las capturas reales son PNG o JPG:

1. Guardalas con el mismo nombre base, por ejemplo `inspecciones.png`.
2. Actualiza las rutas en `public/index.html` (todas las referencias a `./assets/screenshots/...`).

Recomendacion: 1600 px de ancho, sin datos personales reales.
"""

setup_ubuntu = """#!/usr/bin/env bash
# Install the static site on Ubuntu or Debian (AWS EC2 or other VPS).
# Run as root: sudo bash deploy/setup-ubuntu.sh
set -euo pipefail

DOMAIN="archsys.com.ar"
WWW_ROOT="/var/www/${DOMAIN}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PUBLIC_DIR="${REPO_ROOT}/public"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Run this script as root (sudo)."
  exit 1
fi

if [[ ! -d "${PUBLIC_DIR}" ]]; then
  echo "Missing ${PUBLIC_DIR}"
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y nginx certbot python3-certbot-nginx cron rsync

mkdir -p "${WWW_ROOT}"
rsync -a --delete "${PUBLIC_DIR}/" "${WWW_ROOT}/"
chown -R www-data:www-data "${WWW_ROOT}"

install -m 0644 "${SCRIPT_DIR}/nginx-archsys.com.ar.conf" "/etc/nginx/sites-available/${DOMAIN}"
ln -sfn "/etc/nginx/sites-available/${DOMAIN}" "/etc/nginx/sites-enabled/${DOMAIN}"
rm -f /etc/nginx/sites-enabled/default

nginx -t
systemctl enable nginx
systemctl restart nginx

systemctl enable cron
systemctl start cron

echo
echo "Site published at ${WWW_ROOT}"
echo "Next step: issue HTTPS with Let's Encrypt"
echo "  sudo bash ${SCRIPT_DIR}/setup-ssl.sh"
echo
echo "Before issuing the certificate:"
echo "  1. DNS for ${DOMAIN} and www.${DOMAIN} must point to this instance."
echo "  2. The AWS security group must allow 80/tcp and 443/tcp."
"""

setup_ssl = """#!/usr/bin/env bash
# Issue the Let's Encrypt certificate and install the renewal cron.
# Requires DNS pointing to this server and ports 80/443 open.
# Usage: sudo bash deploy/setup-ssl.sh
set -euo pipefail

DOMAIN="archsys.com.ar"
EMAIL="soporte@archsys.com.ar"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Run this script as root (sudo)."
  exit 1
fi

if ! command -v certbot >/dev/null 2>&1; then
  echo "Certbot is not installed. Run setup-ubuntu.sh first."
  exit 1
fi

certbot --nginx \\
  --non-interactive \\
  --agree-tos \\
  --redirect \\
  --email "${EMAIL}" \\
  -d "${DOMAIN}" \\
  -d "www.${DOMAIN}"

install -m 0644 "${SCRIPT_DIR}/certbot-renew.cron" /etc/cron.d/archsys-certbot

certbot renew --dry-run

echo
echo "HTTPS is active at https://${DOMAIN}"
echo "Automatic renewal: /etc/cron.d/archsys-certbot (daily 03:17)"
echo "Hook: systemctl reload nginx"
"""

deploy_sh = """#!/usr/bin/env bash
# Update static files on the server.
# Usage: sudo bash deploy/deploy.sh
set -euo pipefail

DOMAIN="archsys.com.ar"
WWW_ROOT="/var/www/${DOMAIN}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLIC_DIR="$(cd "${SCRIPT_DIR}/../public" && pwd)"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Run this script as root (sudo)."
  exit 1
fi

rsync -a --delete "${PUBLIC_DIR}/" "${WWW_ROOT}/"
chown -R www-data:www-data "${WWW_ROOT}"
echo "Site updated at ${WWW_ROOT}"
"""

cron = """# Automatic Let's Encrypt renewal for archsys.com.ar
# Installed at: /etc/cron.d/archsys-certbot

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Daily at 03:17. Certbot renews only if fewer than 30 days remain.
17 3 * * * root certbot renew --quiet --deploy-hook "systemctl reload nginx"
"""

nginx = """# Public site for Arch Sistemas
# Copy to: /etc/nginx/sites-available/archsys.com.ar
# Enable: ln -s /etc/nginx/sites-available/archsys.com.ar /etc/nginx/sites-enabled/
#
# Certbot adds the HTTPS block when the certificate is issued.

server {
    listen 80;
    listen [::]:80;
    server_name archsys.com.ar www.archsys.com.ar;

    root /var/www/archsys.com.ar;
    index index.html;

    access_log /var/log/nginx/archsys.access.log;
    error_log  /var/log/nginx/archsys.error.log;

    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css application/javascript application/json image/svg+xml;

    add_header X-Content-Type-Options nosniff always;
    add_header X-Frame-Options SAMEORIGIN always;
    add_header Referrer-Policy strict-origin-when-cross-origin always;
    add_header X-XSS-Protection "1; mode=block" always;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location ~* \\.(css|js|ico|png|jpg|jpeg|svg|webp|woff2)$ {
        expires 7d;
        add_header Cache-Control "public, max-age=604800";
        try_files $uri =404;
    }

    location ~ /\\. {
        deny all;
    }
}
"""

out("public/index.html", index)
out("public/js/main.js", js)
out("README.md", readme)
out("public/assets/screenshots/REEMPLAZAR.md", reemplazar)
out("deploy/setup-ubuntu.sh", setup_ubuntu)
out("deploy/setup-ssl.sh", setup_ssl)
out("deploy/deploy.sh", deploy_sh)
out("deploy/certbot-renew.cron", cron)
out("deploy/nginx-archsys.com.ar.conf", nginx)

# Verify UTF-8
sample = (ROOT / "public/index.html").read_text(encoding="utf-8")
assert "Gesti\u00f3n" in sample
assert "C\u00f3rdoba" in sample
print("UTF-8 OK")
