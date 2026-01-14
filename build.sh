#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Compilar TailwindCSS
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --minify

# Arrancar servidor con Gunicorn
gunicorn mivalle_main.wsgi:application

#Otorga permisos de ejecución:
chmod +x build.sh