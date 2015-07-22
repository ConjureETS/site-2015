# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 22, 17, 55, 41, 780027, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
