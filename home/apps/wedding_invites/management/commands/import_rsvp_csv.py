from django.core.management.base import BaseCommand
from apps.wedding_invites.models import Meal, Guest

import csv


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        csv_file = args[0]

        with open(csv_file) as handle:
            rsvps = csv.reader(handle)

            for rsvp in rsvps:
                self.create_rsvp(rsvp)

    def create_rsvp(self, rsvp):
        guest_name, rsvp_option, meal_choice = rsvp

        guest, _ = Guest.objects.get_or_create(name=guest_name)
        if rsvp_option == 'yes':
            meal, _ = Meal.objects.get_or_create(name=meal_choice)
            guest.rsvp.meal = meal

        guest.rsvp.response = rsvp_option

        guest.rsvp.save()
        guest.save()
