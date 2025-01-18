from django.contrib import admin
from myapp import models

@admin.register(models.DetailReview)
class DetailReviewAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        ("pos_date"),
        ("qualification"),
        ("comments"),
        ("active")
    )
    list_display = ["id", "pos_date", "qualification", "comments", "active"]
    list_display_links = ["pos_date", "comments"]
    search_fields = ["pos_date"]
    list_filter = ["active"] 