from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Household(models.Model):
    address = models.TextField(blank=True)
    concrete_guest = models.BooleanField(default=True)
    out_of_town = models.BooleanField(default=False)
    needs_transportation = models.BooleanField(default=False)
    save_the_date_sent = models.BooleanField(default=False)
    invite_sent = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        try:
            if not self.address:
                return self.residents.first().name
        except AttributeError:
            return 'Unlisted Address'
        return self.address


class Guest(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    rsvp = models.CharField(
        max_length=50,
        default='no_response',
        choices=[
            ('no_response', 'No Response'),
            ('yes', 'Yes'),
            ('no', 'No'),
        ]
    )
    child = models.BooleanField(default=False)

    household = models.ForeignKey(
        Household,
        related_name='residents',
    )

    # For admin
    def household_admin_url(self):
        return '<a href="%s">%s</a>' % (
            reverse(
                'admin:wedding_invites_household_change',
                args=(self.household.pk,)
            ),
            str(self.household),
        )
    household_admin_url.allow_tags = True
    household_admin_url.short_description = 'Household Link'

    def concrete_guest(self):
        try:
            return self.household.concrete_guest
        except AttributeError:
            return False

    concrete_guest.boolean = True

    def save_the_date_sent(self):
        try:
            return self.household.save_the_date_sent
        except AttributeError:
            return False

    save_the_date_sent.boolean = True

    def invite_sent(self):
        try:
            return self.household.invite_sent
        except AttributeError:
            return False

    invite_sent.boolean = True

    def out_of_town(self):
        try:
            return self.household.out_of_town
        except AttributeError:
            return False

    out_of_town.boolean = True

    def needs_transportation(self):
        try:
            return self.household.needs_transportation
        except AttributeError:
            return False

    needs_transportation.boolean = True

    def __unicode__(self):
        return self.name
