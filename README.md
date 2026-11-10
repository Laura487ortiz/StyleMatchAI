# StyleMatch AI

StyleMatch AI es un proyecto académico de armario digital inteligente que busca facilitar la organización de prendas de vestir y la generación de recomendaciones de outfits a partir de la ropa disponible del usuario.

## Tecnologías

- Python
- Django
- HTML, CSS y JavaScript
- SQLite
- Modelos de inteligencia artificial para el análisis de prendas y futuras recomendaciones

## Funcionalidades actuales

- Selección y carga de fotografías de prendas.
- Vista previa de imágenes.
- Validación de archivos JPG, JPEG y PNG.
- Almacenamiento local de fotografías.
- Reemplazo y eliminación de fotografías.

## Funcionalidades futuras

- Registro de múltiples prendas.
- Clasificación de prendas mediante modelos preentrenados.
- Organización del armario digital.
- Recomendación de outfits a partir de una prenda seleccionada.

## Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual de Python.
3. Instalar las dependencias con `pip install -r requirements.txt`.
4. Crear el archivo `.env` a partir de `.env.example` y configurar una clave secreta local.
5. Ejecutar `python manage.py migrate`.
6. Ejecutar `python manage.py runserver`.

La aplicación se ejecuta localmente en `http://127.0.0.1:8000/`.

## Estado del proyecto

En desarrollo. Primera fase de implementación de StyleMatch AI.