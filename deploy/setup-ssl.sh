#!/usr/bin/env bash
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

certbot --nginx \
  --non-interactive \
  --agree-tos \
  --redirect \
  --email "${EMAIL}" \
  -d "${DOMAIN}" \
  -d "www.${DOMAIN}"

install -m 0644 "${SCRIPT_DIR}/certbot-renew.cron" /etc/cron.d/archsys-certbot

certbot renew --dry-run

echo
echo "HTTPS is active at https://${DOMAIN}"
echo "Automatic renewal: /etc/cron.d/archsys-certbot (daily 03:17)"
echo "Hook: systemctl reload nginx"
