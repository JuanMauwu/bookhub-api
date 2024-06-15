from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
            app_label = "myapp"
            db_table = "label"
            #ordering = ["pos_date"]
            verbose_name = "Label"
            verbose_name_plural = "Labels"