#!/bin/bash
chmod +x build_files.sh

# Install dependencies
python3 -m pip install -r requirements.txt

# Migrating database...
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collecting static files...
python manage.py collectstatic --noinput

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/