#!/usr/bin/env python
# pass a float argument to this script to set the delay between inserts
import os
import sys
import django
from django.db import transaction
import time

delay = 0
if len(sys.argv) > 1:
    delay = float(sys.argv[1])

sys.path.append(os.path.dirname(__file__))

import overloader

os.environ['DJANGO_SETTINGS_MODULE'] = 'db_locking_example.settings'
django.setup()

while True:
    rec = overloader.models.OverloaderFoo.objects.create()
    rec.bing = "in the future fun is fun, in the future lots of sun, I'll be there it's up to you"
    rec.spang = "you're tired, she's fainting, the scope and the laughter, the future"
    rec.boo = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"
    rec.save()
    print "Added a record"
    time.sleep(delay)
