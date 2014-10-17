# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0009_auto_20141017_0449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='is_kid',
            new_name='child',
        ),
    ]
