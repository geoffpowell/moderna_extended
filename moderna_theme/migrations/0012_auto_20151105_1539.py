# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0011_auto_20151105_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='homepage',
            field=models.ForeignKey(related_name='slides', to='moderna_theme.HomePage'),
        ),
    ]
