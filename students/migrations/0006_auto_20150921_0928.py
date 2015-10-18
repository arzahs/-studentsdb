# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20150919_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthjournal',
            old_name='students',
            new_name='student',
        ),
    ]
