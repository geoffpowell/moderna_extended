# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0004_auto_20151103_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('caption_heading', models.CharField(max_length=200)),
                ('homepage', models.ForeignKey(related_name='slides', to='moderna_theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
