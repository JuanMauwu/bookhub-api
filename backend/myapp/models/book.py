from django.db import models # type: ignore

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, verbose_name="Book author")
    summary = models.TextField(max_length=500, blank=True)
    pos_date = models.DateField()
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
            app_label = "myapp"
            db_table = "book"
            ordering = ["pos_date"]
            verbose_name = "Book"
            verbose_name_plural = "Books"