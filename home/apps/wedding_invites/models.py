from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Custom Querysets
class TableQueryset(models.QuerySet):
    def for_guests(self, guest_queryset):
        guest_ids = [guest.id for guest in guest_queryset.all()]
        return (self
                .select_related('guest__rsvp', 'guest__rsvp__meal')
                .distinct()
                .filter(guests__id__in=guest_ids))


# Models
class Household(models.Model):
    address = models.TextField(blank=True)
    out_of_town = models.BooleanField(default=False)
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


class Table(models.Model):
    identifier = models.CharField(max_length=100)

    objects = TableQueryset.as_manager()

    def __unicode__(self):
        return self.identifier


class Guest(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    child = models.BooleanField(default=False)

    household = models.ForeignKey(
        Household,
        related_name='residents',
    )
    table = models.ForeignKey(
        Table,
        related_name='guests',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
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

    def rsvp_response(self):
        return self.rsvp.get_response_display()

    def table_name(self):
        try:
            return self.table.identifier
        except AttributeError:
            return 'No table assigned'

    def __unicode__(self):
        return self.name


class RSVP(models.Model):
    response = models.CharField(
        max_length=50,
        default='no_response',
        choices=[
            ('no_response', 'No Response'),
            ('yes', 'Yes'),
            ('no', 'No'),
            ('yes_undecided', 'Yes, meal undecided'),
        ]
    )
    special_requests = models.TextField(blank=True)

    guest = models.OneToOneField(Guest, related_name='rsvp')
    meal = models.ForeignKey(
        'Meal',
        related_name='rsvp',
        blank=True,
        null=True,
    )

    def clean(self):
        if self.response == 'yes' and self.meal is None:
            raise ValidationError('A meal is required for a yes response')

        super(RSVP, self).clean()

    def __unicode__(self):
        return self.response

    def guest_name(self):
        try:
            return self.guest.name
        except AttributeError:
            return ''

    def meal_name(self):
        try:
            return self.meal.name
        except AttributeError:
            return ''


class Meal(models.Model):
    name = models.CharField(max_length=255)
    kids_meal = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


@receiver(post_save, sender=Guest)
def create_rsvp_if_none(sender, instance, **kwargs):
    try:
        getattr(instance, 'rsvp')
    except RSVP.DoesNotExist:
        RSVP.objects.create(guest=instance)


@receiver(pre_save, sender=Guest)
def create_household_if_none(sender, instance, **kwargs):
    try:
        getattr(instance, 'household')
    except Household.DoesNotExist:
        instance.household = Household.objects.create()
