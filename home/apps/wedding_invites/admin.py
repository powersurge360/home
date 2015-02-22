from django.contrib import admin

from apps.wedding_invites.models import Household, Guest, Meal, RSVP, Table


# Custom filters
class AddressFilter(admin.SimpleListFilter):
    title = 'Address'

    parameter_name = 'address'

    def lookups(self, request, model_admin):
        return (
            ('has_address', 'Has an Address'),
            ('no_address', 'Needs an Address'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'has_address':
            return queryset.exclude(household__address='')
        elif self.value() == 'no_address':
            return queryset.filter(household__address='')
        else:
            return queryset


class TableIdentiferFilter(admin.SimpleListFilter):
    title = 'Table Identifier'

    parameter_name = 'identifier'

    def lookups(self, request, model_admin):
        identifiers = Table.objects.values('identifier').distinct()

        # Flatten and retrieve values
        identifiers = [
            item
            for identifier in identifiers
            for item in identifier.values()
        ]

        identifiers.append('No table assigned')
        return zip(identifiers, identifiers)

    def queryset(self, request, queryset):
        if self.value() == 'No table assigned':
            return queryset.filter(table__identifier__isnull=True)
        elif self.value() is not None:
            return queryset.filter(table__identifier=self.value())
        else:
            return queryset


# Inlines
class GuestInline(admin.StackedInline):
    model = Guest


# Model admins
class HouseholdAdmin(admin.ModelAdmin):
    inlines = [
        GuestInline
    ]
    list_filter = ('out_of_town',)


class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'household_admin_url',
        'out_of_town',
        'child',
        'save_the_date_sent',
        'invite_sent',
        'rsvp_response',
        'table_name',
    )

    def get_queryset(self, *args):
        queryset = super(GuestAdmin, self).get_queryset(*args)

        return queryset.order_by('household')

    search_fields = (
        'name',
        'household__address',
        'rsvp__response',
    )

    list_filter = (
        'household__out_of_town',
        AddressFilter,
        'child',
        'household__save_the_date_sent',
        'household__invite_sent',
        'rsvp__response',
        TableIdentiferFilter
    )


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'response', 'meal_name')

    list_filter = (
        'meal__name',
        'response',
    )

    search_fields = (
        'guest__name',
        'meal__name',
        'response',
    )


class MealAdmin(admin.ModelAdmin):
    pass


class TableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Household, HouseholdAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Table, TableAdmin)
