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
    
    path(
        "labels",
        views.LabelListAPIView.as_view(),
        name="label-list"
    ),
    
     path(
        "details_reviews",
        views.DetailReviewListAPIView.as_view(),
        name="detail_review-list"
    ),
     
     path(
        "reviews",
        views.ReviewListAPIView.as_view(),
        name="review-list"
    ),
]