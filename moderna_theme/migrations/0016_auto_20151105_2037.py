# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0015_auto_20151105_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkstuff',
            name='block2_link',
        ),
        migrations.RemoveField(
            model_name='linkstuff',
            name='site',
        ),
        migrations.DeleteModel(
            name='Linkstuff',
        ),
    ]
