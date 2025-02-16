from django.db import models
from myapp.models import Language

class Book(models.Model):
    title = models.CharField(max_length=30, unique=True)
    author = models.CharField("Book author", max_length=100)
    summary = models.TextField(max_length=1500, blank=True)
    language = models.ManyToManyField(Language)
    pos_date = models.DateField()
    active = models.BooleanField(default=True)
    

    def __str__(self):    #metodo str para saber como representar una instancia de este modelo en las interfaces
        return self.title
    
    class Meta:
        app_label = "myapp"     # Nombre de la aplicación
        db_table = "book"       # Nombre de la tabla en la base de datos
        ordering = ["id"]       # Como se ordenara en el admin
        verbose_name = "Book"   # Nombre legible singular
        verbose_name_plural = "Books"  # Nombre legible plural