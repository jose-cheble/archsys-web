#!/usr/bin/env bash
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
