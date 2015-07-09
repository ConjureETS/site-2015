# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150616_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('download', models.FileField(upload_to=b'projects_downloads')),
                ('screenshot', models.ImageField(upload_to=b'projects_screenshots')),
                ('members', models.ManyToManyField(to='member.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
