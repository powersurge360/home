# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_auto_20141018_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='seasons',
            field=models.ManyToManyField(related_name=b'menu_items', to='vendors.Season'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='vendor',
            field=models.ForeignKey(related_name=b'vendor', to='vendors.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vendor',
            name='selected',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
