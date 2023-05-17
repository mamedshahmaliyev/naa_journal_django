1. python -m pip install Django
2. django-admin startproject journaling
3. cd journaling
4. python manage.py runserver - this will start local web server
5. python manage.py startapp teachers - create sub application
6. python manage.py makemigrations - create migrations corresponding to created model
7. python manage.py sqlmigrate teachers 0001 - show sql query for migration
8. python manage.py migrate - apply all migrations
9. python manage.py createsuperuser - create admin user