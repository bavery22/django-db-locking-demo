from django.http import HttpResponse
from django.db import transaction
import models

long_text = "In The Future \
It's winter, it's raining \
You're tired, she's fainting \
You're bitter, she's brooding \
But don't be disenchanted \
'Cause you can barely stand it \
The sweep and the grandeur \
The scope and the laughter \
The future, the future \
The future's got it covered \
With what will be discovered \
In the future fun is fun \
In the future, lots of sun \
I'll be there, it's up to you \
You'll be there if you don't do nothing foolish \
You'll love it, I know it \
I know what you like and \
You'll love it, I know it \
We'll need some vintage vino \
So wash your feet and stamp away \
Coming soon and everywhere \
Everyone will walk on air \
Now it seems so far away \
But each day it's getting closer and closer \
Convenience and pleasure \
All blended together \
And culture, and madness \
You think you've seen it all \
You've seen it all except the future"

# Insert a load of spurious records into the database
def index(request):
    global long_text

    response = HttpResponse()

    num_records = int(request.GET.get('num', 1))

    for i in range(0, num_records):
        rec = models.OverloaderFoo.objects.create()
        rec.bing = "in the future fun is fun, in the future lots of sun, I'll be there it's up to you"
        rec.spang = "you're tired, she's fainting, the scope and the laughter, the future"
        rec.boo = long_text
        rec.save()

    plural = ''
    if num_records > 1:
        plural = 's'

    response.write('Added %d record%s\n' % (num_records, plural))

    return response
