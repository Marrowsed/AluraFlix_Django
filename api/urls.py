from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    # Token PATH
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('validate/', validate_token, name='validate_token'),
    # API PATH
    path('videos/', VideoView.as_view(), name="video-view"),
    path('videos/<str:pk>/', VideoDetail.as_view(), name="video-detail"),
    path('categories/', CategoryView.as_view(), name='category-view'),
    path('categories/<str:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<str:pk>/videos/', video_category_detail, name='video-category-detail')

]
