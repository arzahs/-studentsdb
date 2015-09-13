# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=256, verbose_name='Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last Name')),
                ('middle_name', models.CharField(max_length=256, verbose_name='Middle Name', default='', blank=True)),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('ticket', models.CharField(max_length=256, verbose_name='Ticket')),
                ('notes', models.TextField(verbose_name='Notes', default='', blank=True)),
            ],
        ),
    ]
