# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0008_auto_20141017_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='is_kid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp',
            field=models.CharField(default=b'no_response', max_length=50, choices=[(b'no_response', b'No Response'), (b'yes', b'Yes'), (b'no', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='invite_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='save_the_date_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
