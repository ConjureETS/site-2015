# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=b'article_photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
