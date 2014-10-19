# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_auto_20141018_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='services',
            field=models.ManyToManyField(related_name=b'vendors', to=b'vendors.Service'),
        ),
    ]
