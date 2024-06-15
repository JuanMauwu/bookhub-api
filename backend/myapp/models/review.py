from django.db import models
from myapp.models import Book, Label, DetailReview

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    text = models.TextField()
    labels = models.ManyToManyField(Label)
    detail = models.OneToOneField(DetailReview, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.reviewer} about {self.book}"

    class Meta:
        app_label = "myapp"
        db_table = "reviews"
        #ordering = ["pos_date"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"