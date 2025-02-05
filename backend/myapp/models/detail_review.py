from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DetailReview(models.Model):
    pos_date = models.DateField()
    
    # atributo choice para limitar las opciones validas em un campo
    # este debera contener una lista de tuplas (el primer valor de cada tupla es lo que se guarda em db, 
    # y el segundo la opcion que se muestra en el formulario para llenar)
    qualification = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 11)], validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    comments = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Calificacion: {self.qualification} - Comentarios: {self.comments}"
    
    class Meta:
            app_label = "myapp"
            db_table = "detail_review"
            ordering = ["id"]
            verbose_name = "Detail Review"
            verbose_name_plural = "Details Reviews"