from django.db import models

# Create your models here.


class Household(models.Model):
    address = models.TextField(blank=True)
    concrete_guest = models.BooleanField(default=True)
    out_of_town = models.BooleanField(default=False)
    needs_transportation = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        try:
            if not self.address:
                return self.residents.first().name
        except Exception:
            'Unlisted Address'
        return self.address


class Guest(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    household = models.ForeignKey(
        Household,
        related_name='residents',
        null=True,
        blank=True,
    )

    def concrete_guest(self):
        return self.household.concrete_guest

    concrete_guest.boolean = True

    def out_of_town(self):
        return self.household.out_of_town

    out_of_town.boolean = True

    def needs_transportation(self):
        return self.household.needs_transportation

    needs_transportation.boolean = True

    def __unicode__(self):
        return self.name
