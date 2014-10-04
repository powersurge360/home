# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20141004_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='vendor',
            field=models.ForeignKey(related_name=b'questions', default='', to='vendors.Vendor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='price_range',
            field=models.CharField(default='', max_length=300, blank=True),
            preserve_default=False,
        ),
    ]
