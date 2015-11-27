# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OverloaderFoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bing', models.CharField(max_length=255)),
                ('spang', models.CharField(max_length=255)),
                ('boo', models.TextField()),
            ],
        ),
    ]
