echo "Insert records from HTTP and a script to try to throw 'database is locked' error..."

# make num higher to add more records per request
NUM=1
COUNT=0


while true ; do
    let COUNT=$COUNT+1
    TIME_START=`python -c "import time;print int(round(time.time()))"`
    OUTPUT=`curl -s "http://127.0.0.1:8000/overloader/?num=$NUM"`
    TIME_DONE=`python -c "import time;print int(round(time.time()))"`
    echo $OUTPUT "count=$COUNT"
    if [ `echo $OUTPUT | wc -c` != 15 ]; then
	let TIME_DELTA=$TIME_DONE-$TIME_START
	echo "BAD RECORD INSERT on $COUNT attempt took " $TIME_DELTA
	exit -1
    fi
    # we need some space to have access to db during backoff
    sleep `python -c "import time;import random;random.seed(time.time());print random.random()*0.25"`
done
