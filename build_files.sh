#!/bin/bash
chmod +x build_files.sh

# Install dependencies
python3 -m pip install -r requirements.txt

# Migrating database...
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collecting static files...
python3 manage.py collectstatic --noinput

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/