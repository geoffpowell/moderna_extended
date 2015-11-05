# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0007_auto_20151105_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='caption_blurb',
            field=models.CharField(default=b'Blurb for image', max_length=100),
        ),
    ]
