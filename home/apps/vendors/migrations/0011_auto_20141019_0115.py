# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0010_auto_20141018_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='seasons',
            field=models.ManyToManyField(related_name=b'menu_items', to=b'vendors.Season', blank=True),
        ),
    ]
