from django.urls import path, include # type: ignore
from rest_framework import routers # type: ignore
from myapp import views
from .views import BookViewSet, DetailReviewViewSet, LabelViewSet, ReviewViewSet, TagViewSet

router = routers.DefaultRouter()

router.register(r"books",BookViewSet)
router.register(r"details_reviews",DetailReviewViewSet)
router.register(r"labels",LabelViewSet)
router.register(r"reviews",ReviewViewSet)
router.register(r"tags",TagViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


"""
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
    """