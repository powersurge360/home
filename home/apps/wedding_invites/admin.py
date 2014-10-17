from django.contrib import admin

from apps.wedding_invites.models import Household, Guest

# Register your models here.


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

    list_filter = (
        'household__concrete_guest',
        'household__out_of_town',
        'household__needs_transportation',
    )

admin.site.register(Household, HouseholdAdmin)
admin.site.register(Guest, GuestAdmin)
