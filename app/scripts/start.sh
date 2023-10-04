#! /bin/sh

echo start server

python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate
gunicorn delivery_app.wsgi:application --config delivery_app/gunicorn_config.py