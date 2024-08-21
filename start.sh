#!/bin/bash

python manage.py collectstatic --noinput

python manage.py migrate 
gunicorn task.wsgi :application --bind 0.0.0.0:3000 --workers 4 --log-level=info --timeout 120