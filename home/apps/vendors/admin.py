from django.contrib import admin

from apps.vendors.models import Service, Vendor, Question


class QuestionInline(admin.StackedInline):
    model = Question


class VendorAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


class ServiceAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Vendor, VendorAdmin)
