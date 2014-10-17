# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0007_auto_20141004_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='household',
            field=models.ForeignKey(related_name=b'residents', to='wedding_invites.Household'),
        ),
    ]
