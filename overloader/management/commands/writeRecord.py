from django.core.management.base import NoArgsCommand, CommandError

from django.db import OperationalError
import os
import random
import time
import sys
import django
import overloader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ.has_key('TIMEOUT'):
    timeout = float(os.environ['TIMEOUT'])
    DATABASES['default']['OPTIONS'] = { 'timeout': timeout }





class Command(NoArgsCommand):
    args = ""
    help = "prints cows"


    def _createRec(self):
        time_start = int(round(time.time()))
        try:
            self.rec = overloader.models.OverloaderFoo.objects.create()
            time_done = int(round(time.time()))
            self.createTime=time_done-time_start
        except OperationalError as err:
            time_done = int(round(time.time()))
            print "OPERR create>>>>",err
            print "on create count %d operation took %d"% (self.count,time_done-time_start)
            sys.exit()

    def _saveRec(self):
        self.rec.bing = "in the future fun is fun, in the future lots of sun, I'll be there it's up to you"
        self.rec.spang = "you're tired, she's fainting, the scope and the laughter, the future"
        self.rec.boo = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"
        time_start = int(round(time.time()))
        try:
            self.rec.save()
            time_done = int(round(time.time()))
            self.saveTime=time_done-time_start

        except OperationalError as err:
            time_done = int(round(time.time()))
            print "OPERR save>>>>",err
            print "on save count %d operation took %d"% (self.count,time_done-time_start)
            sys.exit()

    def handle_noargs(self, **options):
        self.rec = None
        self.count=0
        delay=.25
        while True:
            self.count=self.count+1
            self._createRec()
            self._saveRec()
            print "Added %d record create took %d sec save took %d sec" % (self.count,self.createTime,self.saveTime)
            time.sleep(random.random()*delay)
