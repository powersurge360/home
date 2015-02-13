# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0011_auto_20150213_0401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='special_requests',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='special_requests',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
