from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path(
        "books",
        views.BookListAPIView.as_view(),
        name="book-list",
    ),
    
    path(
        "tags",
        views.TagListAPIView.as_view(),
        name="tag-list",
    ),
]