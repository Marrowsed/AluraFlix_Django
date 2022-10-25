from django.urls import path
from .views import *

urlpatterns = [
    path('videos', VideoView.as_view(), name="video-view"),
    path('videos/<str:pk>/', VideoDetail.as_view(), name="video-detail"),


]