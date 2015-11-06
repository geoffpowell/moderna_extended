# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0013_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='caption_heading',
            field=models.CharField(default=b'Blurb for this featured image goes here.', max_length=60),
        ),
    ]
