# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0010_auto_20141017_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('kids_meal', models.BooleanField(default=False)),
                ('special_requests', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.CharField(default=b'no_response', max_length=50, choices=[(b'no_response', b'No Response'), (b'yes', b'Yes'), (b'no', b'No')])),
                ('guest', models.ForeignKey(related_name=b'rsvp', to='wedding_invites.Guest')),
                ('meal', models.ForeignKey(related_name=b'rsvp', to='wedding_invites.Meal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='guest',
            name='rsvp',
        ),
    ]
