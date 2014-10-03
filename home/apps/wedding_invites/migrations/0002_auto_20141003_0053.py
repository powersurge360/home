# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
