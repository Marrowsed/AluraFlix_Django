from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import *
from .serializers import VideoSerial


# Create your views here.

class VideoView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerial


class VideoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerial

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Video Deleted", status=status.HTTP_204_NO_CONTENT)
