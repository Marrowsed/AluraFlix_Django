from .models import *
from rest_framework.serializers import *


class CategorySerial(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VideoSerial(ModelSerializer):
    category_name = CharField(read_only=True, source='category')

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category_name']
