from django.contrib import admin
from test_app.models import TestModel

class TestModelAdmin(admin.ModelAdmin):
    change_form_template = "test_app/change_form.html"

    fieldsets = [
        ("First", {
            "classes": ("first", ),
            "fields": ("title", "slug", )
        }),
        ("Second", {
            "classes": ("second", ),
            "fields": ("content", "meta_info", )
        }),
    ]

admin.site.register(TestModel, TestModelAdmin)
