#!/bin/bash
# Instalador completo de HubbaX
set -e

# Instala dependencias si no existen
command -v docker >/dev/null 2>&1 || {
    echo "Docker no está instalado. Por favor instálalo antes de continuar." >&2
    exit 1
}

command -v docker-compose >/dev/null 2>&1 || {
    echo "Docker Compose no está instalado. Por favor instálalo." >&2
    exit 1
}

# Construye e inicia los contenedores
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$ROOT_DIR/deploy"

docker compose up -d

echo "HubbaX se está ejecutando. Usa 'docker compose ps' para verificar los servicios."
