# Arch Sistemas — sitio web

Landing institucional de **Arch Sistemas** para [archsys.com.ar](https://archsys.com.ar).
Presenta el producto de gestión de ascensores. Sitio estático, listo para Ubuntu o Debian en AWS.

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
