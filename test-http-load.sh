echo "Insert records from HTTP and a script to try to throw 'database is locked' error..."

# make num higher to add more records per request
NUM=1

# make SLEEP higher to pause between requests
SLEEP=0

while true ; do
  curl "http://127.0.0.1:8000/overloader/?num=$NUM"
  sleep $SLEEP
done
