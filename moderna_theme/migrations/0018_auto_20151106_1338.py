# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0017_feature_link_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='link_to',
            field=models.URLField(max_length=20, blank=True),
        ),
    ]
