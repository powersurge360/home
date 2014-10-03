# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0002_auto_20141003_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='household',
            field=models.ForeignKey(related_name=b'residents', to='wedding_invites.Household', null=True),
        ),
    ]
