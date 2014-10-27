# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_auto_20141004_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
