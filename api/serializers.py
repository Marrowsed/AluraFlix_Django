from .models import *
from rest_framework.serializers import *


class VideoSerial(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class CategorySerial(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
