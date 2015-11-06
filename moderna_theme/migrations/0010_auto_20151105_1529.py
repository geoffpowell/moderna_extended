# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0009_slide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='homepage',
            field=models.ForeignKey(related_name='slides', verbose_name=b'Slides: upload your images at 1280 X 360 for best results.', to='moderna_theme.HomePage'),
        ),
    ]
