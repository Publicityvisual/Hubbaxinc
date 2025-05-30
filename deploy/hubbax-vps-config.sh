#!/bin/bash
# Configuración del VPS para HubbaX
set -e

# Actualiza el sistema
sudo apt-get update && sudo apt-get upgrade -y

# Instala Docker y Docker Compose si no existen
if ! command -v docker >/dev/null 2>&1; then
    curl -fsSL https://get.docker.com | sh
fi

if ! command -v docker-compose >/dev/null 2>&1; then
    sudo apt-get install -y docker-compose
fi

# Ajusta firewall (ejemplo básico)
sudo ufw allow 80
sudo ufw allow 443

# Crea usuario para HubbaX
sudo useradd -m -s /bin/bash hubbax || true

echo "VPS configurado. Inicia sesión con el usuario 'hubbax' para continuar."
