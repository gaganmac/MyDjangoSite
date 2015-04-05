# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(verbose_name=b'date registered')),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
