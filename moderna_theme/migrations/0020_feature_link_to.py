# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0019_remove_feature_link_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='link_to',
            field=models.URLField(default=datetime.datetime(2015, 11, 6, 21, 42, 59, 838000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
