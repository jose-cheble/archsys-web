# Como reemplazar las capturas ilustrativas

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
