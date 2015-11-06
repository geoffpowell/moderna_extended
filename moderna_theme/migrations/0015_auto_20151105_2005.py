# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
        ('moderna_theme', '0014_feature_caption_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linkstuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('block2_link', models.ForeignKey(related_name='block2_link', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='pages.Page', help_text=b'The page to which block 2 links (no link appears if no selection is made)', null=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
    ]
