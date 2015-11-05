# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moderna_theme', '0005_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
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
        migrations.RemoveField(
            model_name='slider',
            name='homepage',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
