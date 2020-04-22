web: gunicorn coresite.wsgi --access-logfile -
python manage.py collectstatic --noinput
manage.py migrate