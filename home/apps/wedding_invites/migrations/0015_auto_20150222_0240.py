# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0014_auto_20150213_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifer', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='household',
            name='concrete_guest',
        ),
        migrations.RemoveField(
            model_name='household',
            name='needs_transportation',
        ),
        migrations.AddField(
            model_name='guest',
            name='table',
            field=models.ForeignKey(related_name=b'guests', blank=True, to='wedding_invites.Table', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='response',
            field=models.CharField(default=b'no_response', max_length=50, choices=[(b'no_response', b'No Response'), (b'yes', b'Yes'), (b'no', b'No'), (b'yes_undecided', b'Yes, meal undecided')]),
        ),
    ]
