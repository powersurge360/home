# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0006_auto_20141018_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='price_range',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
