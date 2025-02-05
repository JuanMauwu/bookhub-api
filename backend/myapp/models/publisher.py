from django.db import models
from myapp.models import Book   

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    founded = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField(max_length=200)
    books = models.ManyToManyField(Book)
    address = models.JSONField()
    active = models.BooleanField()
    email = models.EmailField(max_length=254)
    revenue = models.DecimalField(max_digits=500, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "myapp"      
        db_table = "publisher" 
        ordering = ["id"] 
        verbose_name = "Publisher"   
        verbose_name_plural = "Publishers"