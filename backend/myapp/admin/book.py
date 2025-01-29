from django.contrib import admin
from myapp import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        (("title"), #campos que se muestran para ser llenados
        ("author")),
        ("summary"),
        ("pos_date"),
        ("active"),
    )
    
    list_display = ["id", "title", "author", "summary", "pos_date", "active"] #lo que se mostrara en el listado de objetos creados
    list_display_links = ["title", "author"]                            #campos que se convertiran en enlace para ver detalles o modificarlos
    search_fields = ["title", "author", "summary"]                      #especifica por cuales campos se puede buscar
    list_filter = ["active","author"]                                   #los campos por los que queremos filtrar la info
    list_editable = ["active"]                                 #para editar directamente desde el listado de objetos
    list_per_page = 50                                                  #cuantos elementos queremos  ostrar por pagina