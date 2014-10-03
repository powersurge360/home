# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0005_auto_20141003_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='concrete_guest',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='needs_transportation',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='out_of_town',
        ),
    ]
