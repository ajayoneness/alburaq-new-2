#!/usr/bin/env bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn alburaq_project.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --workers ${WEB_CONCURRENCY:-2} \
  --timeout 120
