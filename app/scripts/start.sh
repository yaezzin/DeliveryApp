#! /bin/sh

echo start server

python manage.py collectstatic
python manage.py migrate
gunicorn delivery_app.wsgi:application --config delivery_app/gunicorn_config.py