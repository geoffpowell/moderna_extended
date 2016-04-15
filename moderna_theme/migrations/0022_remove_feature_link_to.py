# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0021_auto_20151106_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='link_to',
        ),
    ]
