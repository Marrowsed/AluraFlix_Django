from .models import *
from rest_framework.serializers import *


class CategorySerial(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VideoSerial(ModelSerializer):
    category_name = CharField(read_only=False, source='category', required=False)

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category_name']

    def create(self, validated_data):
        if validated_data.get('category') is not None:
            category = validated_data.pop('category')
            name = Category.objects.get(title=category)
        else:
            name = Category.objects.get_or_create(title="LIVRE", color="white")
        video = Video.objects.create(**validated_data, category=name)
        return video


class PlaylistSerial(ModelSerializer):
    videos = VideoSerial(
        many=True,
        read_only=True,
     )

    class Meta:
        model = Category
        fields = ['id', 'title', 'color', 'videos']
