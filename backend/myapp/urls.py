from django.urls import path, include # type: ignore
from rest_framework import routers # type: ignore
from myapp import views

app_name = "myapp"

router = routers.DefaultRouter()

urlpatterns = [

    #book
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path("book/<str:id>/", views.BookDetailAPIView.as_view(), name="book-detail"),
    
    #detail_review
    path('detail_reviews/', views.DetailReviewListCreateAPIView.as_view(), name='detail-review-list-create'),
    path("detail_review/<str:id>/", views.DetailReviewDetailAPIView.as_view(), name="detail-review-detail"),

    #label
    path('labels/', views.LabelListCreateAPIView.as_view(), name='label-list-create'),
    path("label/<str:id>/", views.LabelDetailAPIView.as_view(), name="label-detail"),
    
    #publisher
    path('publishers/', views.PublisherListCreateAPIView.as_view(), name='publisher-list-create'),
    path("publisher/<str:id>/", views.PublisherDetailAPIView.as_view(), name="publisher-detail"),
    
    #review
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path("review/<str:id>/", views.ReviewDetailAPIView.as_view(), name="review-detail"),
    
    #tag
    path('tags/', views.TagListCreateAPIView.as_view(), name='tag-list-create'),
    path("tag/<str:id>/", views.TagDetailAPIView.as_view(), name="tag-detail"),
    
]