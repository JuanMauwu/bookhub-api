# django-benniger

Comandos para iniciar el proyecto:

- Abrir terminal
- Abrir docker
- docker compose up backend (inicializa el contenedor)

Abrir sitio administrativo:

- http://localhost:8000/admin/

Endpoint o rutas de APIs:

- http://localhost:8000/api/v1/books
- http://localhost:8000/api/v1/tags

Comando para el test:

- docker compose exec backend python manage.py test myapp.tests

Hacer migraciones(despues de crear o modificar un modelo):

- docker compose exec backend python manage.py makemigrations myapp

- docker compose exec backend python manage.py migrate myapp
