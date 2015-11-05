# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0006_auto_20151105_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='caption_heading',
            field=models.CharField(max_length=30),
        ),
    ]
