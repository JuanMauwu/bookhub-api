from django.contrib import admin
from myapp import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        ("title"),
        ("author"),
        ("summary"),
        ("pos_date"),
        ("active"),
    )
    list_display = ["title", "author", "summary", "pos_date", "active"]
    list_display_link = ["title", "author", "summary", "pos_date", "active"]
    search_fields = ["title"]
    list_filter = ["title"]