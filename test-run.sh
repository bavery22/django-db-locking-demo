reset

echo "Clean out db..."
rm -f  db.sqlite3

echo "Applying migrations..."
./manage.py migrate


echo "Start server..."
./manage.py runserver
