from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
            app_label = "myapp"
            db_table = "tag"
            verbose_name = "Tag"
            verbose_name_plural = "Tags"