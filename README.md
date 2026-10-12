# TravelDream 🌎

Aplicación web de turismo desarrollada con Django, MariaDB y Django REST Framework. Permite administrar destinos turísticos, mostrar información de viajes y gestionar imágenes.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MariaDB
- PyMySQL
- HTML y CSS
- Pillow para el manejo de imágenes

## Requisitos previos

Antes de ejecutar el proyecto, instala:

- Python compatible con las dependencias del proyecto.
- Git.
- MariaDB.
- Visual Studio Code (opcional, para editar el código).

## 1. Descargar el proyecto

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/jhonmm7/TravelDream.git
cd TravelDream
```

## 2. Crear un entorno virtual

En Windows, ejecuta:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Si utilizas CMD en lugar de PowerShell, activa el entorno con:

```cmd
venv\Scripts\activate.bat
```

## 3. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

```bash
python -m pip install -r requirements.txt
```

## 4. Configurar MariaDB

Crea una base de datos llamada `turismo_db` en MariaDB.

Configura las siguientes variables de entorno según tu instalación:

- `DB_NAME`: nombre de la base de datos.
- `DB_USER`: usuario de MariaDB.
- `DB_PASSWORD`: contraseña del usuario.
- `DB_HOST`: servidor de MariaDB, normalmente `localhost`.
- `DB_PORT`: puerto de MariaDB, normalmente `3306`.
- `DJANGO_SECRET_KEY`: clave secreta privada de Django.

No publiques contraseñas ni claves secretas en GitHub.

## 5. Crear las tablas

Ejecuta las migraciones:

```bash
python manage.py migrate
```

Las migraciones crean las tablas necesarias, pero no restauran los destinos ni las imágenes de una instalación anterior.

## 6. Iniciar el servidor

Ejecuta:

```bash
python manage.py runserver
```

Abre en el navegador:

http://127.0.0.1:8000/

## API REST

La API permite consultar y administrar destinos turísticos.

| Método | Endpoint | Función |
|---|---|---|
| GET | `/api/destinos/` | Listar destinos |
| POST | `/api/destinos/` | Crear un destino |
| GET | `/api/destinos/<id>/` | Consultar un destino |
| PUT | `/api/destinos/<id>/` | Actualizar un destino |
| DELETE | `/api/destinos/<id>/` | Eliminar un destino |

Las operaciones de creación, actualización y eliminación requieren autenticación según la configuración actual del proyecto.

## Imágenes

Las imágenes se guardan en el directorio configurado para archivos multimedia. Para conservar las imágenes de una instalación anterior, también debes respaldar esos archivos.

## Repositorio

GitHub: https://github.com/jhonmm7/TravelDream