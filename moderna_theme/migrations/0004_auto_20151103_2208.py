# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0003_auto_20151103_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='heading',
            field=models.CharField(default=b'Super Cool Heading', help_text=b'Heading for paragraph', max_length=100),
        ),
    ]
