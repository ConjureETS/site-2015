# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='download',
            field=models.FileField(null=True, upload_to=b'projects_downloads', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to='member.Member', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(null=True, upload_to=b'projects_screenshots', blank=True),
            preserve_default=True,
        ),
    ]
