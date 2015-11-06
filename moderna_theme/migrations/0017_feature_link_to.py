# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0016_auto_20151105_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='link_to',
            field=models.URLField(default=b'url here', max_length=100),
        ),
    ]
