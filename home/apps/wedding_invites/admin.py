from django.contrib import admin

from apps.wedding_invites.models import Household, Guest

# Register your models here.


# Inlines
class GuestInline(admin.StackedInline):
    model = Guest


class HouseholdAdmin(admin.ModelAdmin):
    inlines = [
        GuestInline
    ]


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'household',)

admin.site.register(Household, HouseholdAdmin)
admin.site.register(Guest, GuestAdmin)
