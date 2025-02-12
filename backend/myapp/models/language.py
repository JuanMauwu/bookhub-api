from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=20, unique=True)
    flag = models.ImageField(upload_to="flags/")
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "myapp"
        db_table = "language"
        ordering = ["id"]
        verbose_name = "Language"
        verbose_name_plural = "Languages"    