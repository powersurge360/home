# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('concrete_guest', models.BooleanField(default=True)),
                ('out_of_town', models.BooleanField(default=False)),
                ('needs_transportation', models.BooleanField(default=False)),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField()),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='guest',
            name='household',
            field=models.ForeignKey(related_name=b'residents', to='wedding_invites.Household'),
            preserve_default=True,
        ),
    ]
