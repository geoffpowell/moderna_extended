# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0002_remove_homepage_paragraph_blurb'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='paragraph_blurb',
            field=models.CharField(default=b'This is a test. I am a robot.', help_text=b'Paragraph under the top heading', max_length=600),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading',
            field=mezzanine.core.fields.RichTextField(default=b'Super Cool Heading', help_text=b'Heading for paragraph', max_length=100),
        ),
    ]
