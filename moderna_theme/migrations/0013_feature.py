# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0012_auto_20151105_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('caption_blurb', models.CharField(default=b'Blurb for this featured image goes here.', max_length=100)),
                ('homepage', models.ForeignKey(related_name='features', to='moderna_theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
