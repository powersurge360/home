# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0015_auto_20150222_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='identifer',
            new_name='identifier',
        ),
    ]
