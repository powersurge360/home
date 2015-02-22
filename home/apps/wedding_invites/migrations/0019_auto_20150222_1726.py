# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0018_table_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='identifier',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
