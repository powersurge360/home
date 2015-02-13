# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0012_auto_20150213_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='meal',
            field=models.ForeignKey(related_name=b'rsvp', blank=True, to='wedding_invites.Meal', null=True),
        ),
    ]
