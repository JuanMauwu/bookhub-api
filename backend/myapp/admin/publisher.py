from django.contrib import admin
from myapp import models

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):

    icon_name = "icons/imagenes"
    fields = (
        ("name"),
        ("founded"),
        ("website"),
        ("books"),
        ("address"),
        ("email"),
        ("revenue"),
        ("active")
    )
    
    list_display = [
        "id",
        "name", 
        "founded", 
        "website",
        "address",
        "active",
        "email",
        "revenue" 
    ]
    list_display_links = ["name"]
    search_fields = ["name", "books"]
    list_filter = ["active"]
    filter_horizontal = ["books"]
    #list_per_page = 1