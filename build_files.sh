echo "Building project packages..."
python -m pip install -r requirements.txt

echo "Migrating database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput