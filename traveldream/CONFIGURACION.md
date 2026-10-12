

CONFIGURACIÓN DE TRAVELDREAM

1. Instalar las dependencias:
   pip install -r requirements.txt

2. Crear la base de datos MariaDB:
   turismo_db

3. Configurar las variables de entorno:
   DB_NAME=turismo_db
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=3306
   DJANGO_SECRET_KEY=generar_una_clave_secreta

4. Aplicar las migraciones:
   python manage.py migrate

5. Iniciar el servidor:
   python manage.py runserver

Nota: esta guía no contiene credenciales reales.
