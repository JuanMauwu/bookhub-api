from django.contrib import admin # type: ignore
from myapp import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        ("book"),
        ("reviewer"),
        ("text"),
        ("labels"),
        ("detail"),
        ("active")
    )
    
    list_display = ["book", "reviewer", "text", "detail", "active"] #dice que label no puede ser utilizado en list_display porque es un campo ManyToManyField
    list_display_links = ["book"]
    search_fields = ["reviewer"]
    list_filter = ["book"]