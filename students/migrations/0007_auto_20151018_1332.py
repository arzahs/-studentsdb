# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20150921_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Groups', 'verbose_name': 'Group'},
        ),
        migrations.AlterModelOptions(
            name='monthjournal',
            options={'verbose_name_plural': 'MonthJournals', 'verbose_name': 'MonthJournal'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Students', 'verbose_name': 'Student'},
        ),
    ]
