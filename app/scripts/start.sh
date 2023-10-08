#! /bin/sh

echo start server

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn delivery_app.wsgi:application --config delivery_app/gunicorn_config.py