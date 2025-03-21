
# Tarea 2 - Análisis y Diseño de Sistemas 1

Este proyecto es una aplicación web sencilla que muestra mi nombre, carnet y curso en una página HTML utilizando FastAPI.

## Instalación en Ambiente Local
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Navega a la carpeta del proyecto:
   ```bash
   cd Tarea2
   ```

3. Crea una imagen de Docker:
   ```bash
   docker build -t tarea2-app .
   ```

4. Detén cualquier contenedor anterior que esté utilizando el puerto 80:
   ```bash
   docker ps
   docker stop <CONTAINER_ID>
   docker rm <CONTAINER_ID>
   ```

5. Ejecuta el contenedor en el puerto 80:
   ```bash
   docker run -d -p 80:80 tarea2-app
   ```

6. Abre tu navegador en [http://localhost](http://localhost).

## Despliegue en Fly.io
1. Instala Fly.io si aún no lo tienes:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. Crea una nueva app en Fly.io:
   ```bash
   fly launch
   ```

3. Sigue las instrucciones para configurar el despliegue.

4. Usa el siguiente comando para desplegar la aplicación:
   ```bash
   fly deploy
   ```

5. Tu aplicación estará disponible en el enlace proporcionado por Fly.io.

---

Si tienes algún error o quieres optimizar algo, avísame. 🚀
