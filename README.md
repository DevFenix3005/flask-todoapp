# Aplicación To-Do con Flask

Una aplicación sencilla de tareas (To-Do) construida con Flask y SQLite.

## Estructura del Proyecto

Este proyecto sigue el patrón estándar de fábrica de aplicaciones de Flask (application factory). 
Incluye autenticación (registro/inicio de sesión) y una funcionalidad central de tareas donde los usuarios pueden administrar sus propias actividades.

- `todoapp/`: El paquete principal de la aplicación.
  - `routes/`: Contiene las definiciones de las rutas (`auth_route.py` y `todo_route.py`).
  - `templates/`: Plantillas HTML para las vistas.
  - `database.py`: Lógica para la conexión e inicialización de la base de datos.
  - `schemas.sql`: Esquema de la base de datos SQLite.
  - `todo_repo.py`: Capa de repositorio para interactuar con los elementos de la lista de tareas.

## Requisitos Previos

- Python 3.8+ (o [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) para manejo de entornos)
- [Flask](https://flask.palletsprojects.com/)
- [Ngrok](https://ngrok.com/) (opcional, para exponer la app a internet)

## Instalación

1. **Clonar el repositorio** (si aún no lo has hecho):
   ```bash
   git clone <url-del-repositorio>
   cd flask-todoapp
   ```

2. **Crear y activar un entorno virtual** (elige una opción):

   **Opción A: Usando `venv` (estándar de Python)**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

   **Opción B: Usando `conda`**
   ```bash
   conda create -n flask-todoapp python=3.10
   conda activate flask-todoapp
   ```

3. **Instalar la aplicación y sus dependencias**:
   ```bash
   pip install -e .
   ```

## Configuración y Ejecución

1. **Inicializar la base de datos**:
   Esto ejecutará el archivo `schemas.sql` para crear las tablas necesarias en tu base de datos de SQLite.
   ```bash
   flask --app todoapp init-db
   ```

2. **Ejecutar el servidor de desarrollo**:
   ```bash
   flask --app todoapp run --debug
   ```

3. **Acceder a la aplicación localmente**:
   Abre tu navegador y dirígete a [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Exponer la aplicación a Internet con Ngrok

Si deseas compartir tu aplicación con alguien más a través de Internet, puedes usar `ngrok` para crear un túnel seguro hacia tu servidor local.

1. Asegúrate de tener el servidor de Flask corriendo en una terminal (`flask --app todoapp run --debug`).
2. Abre **otra terminal** y ejecuta el siguiente comando:
   ```bash
   ngrok http 5000
   ```
3. Ngrok generará una interfaz en la terminal donde mostrará una URL pública (por ejemplo: `https://abcd-123.ngrok-free.app`). Puedes compartir esa URL para que cualquier persona acceda a tu aplicación To-Do desde internet.

## Construir la aplicación (Wheel)

Si deseas empaquetar tu aplicación para distribuirla o instalarla en otro lugar, puedes generar un archivo `wheel` (.whl) de Python.

1. Asegúrate de tener instalada la herramienta `build`:
   ```bash
   pip install build
   ```

2. Ejecuta el comando de construcción en el directorio raíz del proyecto (donde se encuentra `pyproject.toml`):
   ```bash
   python -m build --wheel
   ```

3. El archivo `.whl` resultante se guardará dentro de una nueva carpeta llamada `dist/`.

## Características

- Registro y autenticación de usuarios.
- Crear, leer, actualizar y eliminar (CRUD) tareas.
- Listas de tareas personales (cada usuario solo ve sus propias tareas).
- Base de datos en SQLite.
