#!/bin/bash

echo "Building the project"
python3.11.4 pip install -r requirements.txt

echo "Makemigration..."

python3.11.4 manage.py makemigrations --noinput
python3.11.4 manage.py migrate --noinput

echo "Collect static"
python3.11.4 manage.py collectstatic --noinput --clear



