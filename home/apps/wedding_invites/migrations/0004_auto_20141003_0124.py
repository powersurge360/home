# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0003_auto_20141003_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='concrete_guest',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='needs_transportation',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='out_of_town',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='household',
            field=models.ForeignKey(related_name=b'residents', blank=True, to='wedding_invites.Household', null=True),
        ),
    ]
