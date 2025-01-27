from django.contrib import admin
from myapp import models

@admin.register(models.Label)
class LabelAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        ("name"),
        ("description"),
        ("active")
    )
    list_display = ["id", "name", "description"]
    list_display_links = ["name", "description"]
    search_fields = ["name"]
    list_filter = ["active"]