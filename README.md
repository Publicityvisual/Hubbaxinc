# HubbaX Inc

HubbaX Inc es una plataforma social inteligente que integra IA en cada uno de sus módulos. Este repositorio contiene un ejemplo básico para iniciar el proyecto y desplegarlo mediante Docker. Ahora incluye un servicio que se conecta con los modelos de Hugging Face para generar contenido de forma sencilla.

## Requisitos
- Docker 20+
- Docker Compose 1.29+
- Sistema operativo basado en Linux

## Instalación rápida
1. Clona este repositorio en tu servidor:
   ```bash
   git clone <repo-url> hubbax-inc
   cd hubbax-inc
   ```
2. Ejecuta el script de instalación, el cual prepara el entorno y lanza los contenedores:
   ```bash
   bash scripts/instala-hubbax-suite.sh
   ```
3. Crea un archivo `.env` con tu token de Hugging Face y la URL del modelo (opcional):
   ```bash
   echo "HF_API_TOKEN=tu_token" > .env
  echo "HF_MODEL_URL=https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1" >> .env
   ```
Los contenedores instalarán sus dependencias automáticamente la primera vez que se inicien.

Una vez levantado el proyecto visita `http://localhost:3000/builder.html` para probar el constructor de páginas que utiliza la IA para generar HTML.
El backend estará disponible en `http://localhost:3000` y el servicio de IA en `http://localhost:8000`.

## Despliegue manual
Si prefieres hacerlo manualmente, sigue estos pasos:
1. Construye y levanta los servicios definidos en `docker-compose.yml`:
   ```bash
   docker compose -f deploy/docker-compose.yml up -d
   ```
   El contenedor `ai` necesita la variable de entorno `HF_API_TOKEN` con tu token de Hugging Face para poder generar contenido. Puedes usar `HF_MODEL_URL` para cambiar el modelo sin modificar el código.
2. Accede al contenedor `backend` para iniciar el servidor (según el framework que utilices).

## Estructura del repositorio
- `deploy/docker-compose.yml`: configuración de contenedores para base de datos, backend y otros servicios.
- `deploy/hubbax-vps-config.sh`: script de ejemplo para preparar tu VPS con Docker y ajustes básicos.
- `scripts/instala-hubbax-suite.sh`: instalador que clona dependencias y ejecuta Docker Compose.
- `versions/`: archivos JSON con versiones de módulos.
- `frontend/`: archivos estáticos incluyendo `builder.html` para crear páginas con IA.
- `backend/`: pequeño servidor Express que expone la API.

## Licencia
El proyecto se distribuye bajo la licencia MIT. Revisa el archivo [LICENSE](LICENSE) para más información.
