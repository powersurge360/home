# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0016_auto_20150222_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='table',
            field=models.ForeignKey(related_name=b'guests', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wedding_invites.Table', null=True),
        ),
    ]
