from django.db import models

class OverloaderFoo(models.Model):
    bing = models.CharField(max_length=255)
    spang = models.CharField(max_length=255)
    boo = models.TextField()
