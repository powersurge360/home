from django.contrib import admin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

from ckeditor.widgets import CKEditorWidget

# Register your models here.


class FlatPageForm(FlatpageForm):
    class Meta:
        model = FlatPage
        exclude = [] 
        widgets = {
            'content': CKEditorWidget(config_name='default'),
        }


class CustomFlatPageAdmin(FlatPageAdmin):
    form = FlatPageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
