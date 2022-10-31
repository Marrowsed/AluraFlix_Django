from django.urls import path
from .views import *

urlpatterns = [
    path('videos/', VideoView.as_view(), name="video-view"),
    path('videos/<str:pk>/', VideoDetail.as_view(), name="video-detail"),
    path('categories/', CategoryView.as_view(), name='category-view'),
    path('categories/<str:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<str:pk>/videos/', video_category_detail, name='video-category-detail')


]