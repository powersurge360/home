from django.contrib import admin

from apps.wedding_invites.models import Household, Guest


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


# Inlines
class GuestInline(admin.StackedInline):
    model = Guest
    list_filter = ('concrete_guest',)


class HouseholdAdmin(admin.ModelAdmin):
    inlines = [
        GuestInline
    ]
    list_filter = ('concrete_guest', 'out_of_town', 'needs_transportation',)


class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'household_admin_url',
        'concrete_guest',
        'out_of_town',
        'needs_transportation',
    )

    def queryset(self, *args):
        queryset = super(GuestAdmin, self).queryset(*args)

        return queryset.order_by('household')

    search_fields = (
        'name',
        'household__address',
    )

    list_filter = (
        'household__concrete_guest',
        'household__out_of_town',
        'household__needs_transportation',
        AddressFilter,
    )

admin.site.register(Household, HouseholdAdmin)
admin.site.register(Guest, GuestAdmin)
