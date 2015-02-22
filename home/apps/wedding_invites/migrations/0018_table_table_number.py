# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0017_auto_20150222_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
