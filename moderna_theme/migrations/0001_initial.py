# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('paragraph_blurb', models.CharField(default=b'This is a test. I am a robot.', help_text=b'Paragraph under the top heading', max_length=600)),
                ('heading', models.CharField(default=b'Super Cool Heading', help_text=b'Heading for paragraph', max_length=100)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
            bases=('pages.page', models.Model),
        ),
    ]
