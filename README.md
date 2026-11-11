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

## Datasets y Modelos Disponibles

- [Registro de múltiples prendas polyvore-dataset.](https://github.com/xthan/polyvore-dataset)
- [Organización del armario digital Fashionism-Machine-Learning.](https://github.com/Fashionism-Bangkit-Capstone/Fashionism-Machine-Learning)
- [Recomendación de outfits a partir de una prenda seleccionada DeepFashion2.](https://github.com/switchablenorms/deepfashion2)
- [Modelo pre entrenado fashion-Clip](https://github.com/patrickjohncyh/fashion-clip)
- [Modelo experimental](https://github.com/lzcn/outfit-recommendation)

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

- [Tablero en Notion (unicamente para el equipo de trabajo)](https://app.notion.com/p/dd6c1deb16af4af0b68c611898c135fa?v=42056935f0f54eee80f9b86972098bec)
- [Dataset de imágenes autorizadas](https://drive.google.com/file/d/1U0bP4_AB2dBTK0ec_VlCiezHnoi5-RdF/view?usp=sharing)
- 
