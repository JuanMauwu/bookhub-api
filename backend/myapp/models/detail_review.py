from django.db import models

class DetailReview(models.Model):
    pos_date = models.DateField()
    qualification = models.IntegerField(default=1)
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