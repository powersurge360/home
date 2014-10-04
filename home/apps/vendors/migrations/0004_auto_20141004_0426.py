# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20141004_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='services',
            field=models.ManyToManyField(related_name=b'vendors', null=True, to=b'vendors.Service', blank=True),
        ),
    ]
