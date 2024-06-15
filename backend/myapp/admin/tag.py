from django.contrib import admin
from myapp import models

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        ("name"),
        ("active")
    )
    
    list_display = ["name", "active"]
    list_display_link = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]