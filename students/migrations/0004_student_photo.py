# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20150913_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, verbose_name='Photo', upload_to=''),
        ),
    ]
