#!/bin/bash

echo "Building the project"
pip install -r requirements.txt

echo "Makemigration..."

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect static"
python manage.py collectstatic --noinput --clear



