# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150616_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(default=False, max_length=50),
            preserve_default=False,
        ),
    ]
