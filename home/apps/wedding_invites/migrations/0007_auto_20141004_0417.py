# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0006_auto_20141003_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
