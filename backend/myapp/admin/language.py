from django.contrib import admin
from myapp import models

#utils.html es un modulo de django para trabajar con html en este caso de forma segura
#mark_safe es una funcion que convierte una cadena de texto en una cadena confiable para que Django no interprete los caracteres HTML literalmente
from django.utils.html import mark_safe 


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        (("name"),
         ("code")),
        ("flag"),
        ("active")
    )
    
    list_display = ["name", "code", "flag_preview", "flag", "active"]
    list_display_links = ["name", "code"]
    search_fields = ["name"]
    list_filter = ["active"]
    
    def flag_preview(self, obj):
        if obj.flag:
            return mark_safe(f"<img src='{obj.flag.url}' width='50' height='30' />")
        return "No image"
    
    #.url es un atributo especial de los campos de tipo imagenField y FileField, en este caso nos da la URL de la imagen de instancia actual para acceder desde el navegador