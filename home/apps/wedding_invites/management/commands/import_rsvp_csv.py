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

        try:
            guest = Guest.objects.get(name=guest_name)
            meal = Meal.objects.get(name=meal_choice)
            guest.rsvp.response = rsvp_option
            guest.rsvp.meal = meal

            guest.rsvp.save()
            guest.save()
        except (Guest.DoesNotExist, Meal.DoesNotExist):
            pass
