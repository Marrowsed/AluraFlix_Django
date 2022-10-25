from .models import *
from rest_framework.serializers import *


class VideoSerial(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
