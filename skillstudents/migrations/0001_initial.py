# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsStudents',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=150)),
                ('cdate', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
