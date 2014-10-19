from django.contrib import admin

from apps.vendors.models import Service, Vendor, MenuItem, MenuCategory


class VendorAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


class MenuItemAdmin(admin.ModelAdmin):
    pass


class MenuCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
