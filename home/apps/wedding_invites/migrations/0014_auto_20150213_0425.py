# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0013_auto_20150213_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='guest',
            field=models.OneToOneField(related_name=b'rsvp', to='wedding_invites.Guest'),
        ),
    ]
