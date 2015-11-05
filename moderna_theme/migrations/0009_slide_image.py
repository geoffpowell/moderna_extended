# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0008_slide_caption_blurb'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True),
        ),
    ]
