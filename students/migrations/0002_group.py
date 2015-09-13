# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Notes')),
                ('leader', models.OneToOneField(to='students.Student', blank=True, null=True, verbose_name='Leader')),
            ],
        ),
    ]
