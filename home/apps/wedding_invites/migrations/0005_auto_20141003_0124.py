# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_bools_to_household(apps, schema_editor):
    Household = apps.get_model('wedding_invites', 'Household')

    for household in Household.objects.select_related('residents').all():
        resident = household.residents.first()
        household.concrete_guest = resident.concrete_guest
        household.out_of_town = resident.out_of_town
        household.needs_transportation = resident.needs_transportation
        household.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invites', '0004_auto_20141003_0124'),
    ]

    operations = [
        migrations.RunPython(move_bools_to_household)
    ]
