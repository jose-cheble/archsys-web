#!/usr/bin/env bash
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
