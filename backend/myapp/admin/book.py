from django.contrib import admin
from myapp import models
from django.utils.html import format_html

@admin.register(models.Book)        #decorador para registrar el modelo en django administration para que aparezca y sea manejable
class BookAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        (("title"), #campos que se muestran para ser llenados   
        ("author")),
        ("summary"),
        ("pos_date"),
        ("language"),
        ("active"),
    )
    
    list_display = ["id", "title", "author", "summary", "languages", "pos_date", "active"]   #lo que se mostrara en el listado de objetos creados
    list_display_links = ["title", "author"]                                    #campos que se convertiran en enlace para ver detalles o modificarlos
    search_fields = ["title", "author", "summary"]                              #especifica por cuales campos se puede buscar
    list_filter = ["active","author"]                                           #los campos por los que queremos filtrar la info
    list_editable = ["active"]                                                  #para editar directamente desde el listado de objetos
    list_per_page = 50                                                          #cuantos elementos queremos  ostrar por pagina
    
    #falta entender esta monda
    def languages(self, obj):
        """Muestra las banderas de los idiomas en la lista de libros"""
        flags = [
            format_html('<img src="{}" width="25px" height="15px"/>', lang.flag.url)
            for lang in obj.language.all() if lang.flag
        ]
        return format_html(" ".join(flags)) if flags else "-"