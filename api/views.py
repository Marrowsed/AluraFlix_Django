from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.

class VideoView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerial

    def get_queryset(self):
        queryset = Video.objects.all()
        video = self.request.query_params.get('search')
        if video is not None:
            queryset = queryset.filter(title__icontains=video)
        return queryset


class VideoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerial

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Video Deleted", status=status.HTTP_204_NO_CONTENT)


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerial


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerial

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Category Deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def video_category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    video = Video.objects.filter(category=category)
    serializer = VideoSerial(video, many=True)
    return Response(serializer.data) if len(video) > 0 else Response("No Videos in this Category",
                                                                     status=status.HTTP_404_NOT_FOUND)
