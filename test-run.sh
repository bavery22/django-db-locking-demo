reset

echo "Applying migrations..."
./manage.py migrate

echo "Clean out spurious records table..."
sqlite3 db.sqlite3 "DELETE FROM overloader_overloaderfoo"

echo "Start server..."
./manage.py runserver

