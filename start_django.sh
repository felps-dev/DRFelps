#!/bin/bash

# Wait mysql start
# echo Wait mysql start.
# sleep 15

# Apply database migrations
echo Running Migrate.
python manage.py migrate

# Loading Fixtures of Permissao
python manage.py loaddata permissao

# Collect static files
echo Running Collectstatic.
python manage.py collectstatic --noinput


python manage.py runserver 0.0.0.0:8000