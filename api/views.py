from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


# Create your views here.


class VideoView(ListCreateAPIView):
    """Endpoint to GET/POST a Video"""
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerial

    def get_queryset(self):
        queryset = Video.objects.all()
        video = self.request.query_params.get('search')
        if video is not None:
            queryset = queryset.filter(title__icontains=video)
        return queryset


class VideoDetail(RetrieveUpdateDestroyAPIView):
    """Endpoint to GET/PUT/PATCH/DELETE a Video ID"""
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerial

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Video Deleted", status=status.HTTP_204_NO_CONTENT)


class CategoryView(ListCreateAPIView):
    """Endpoint to GET/POST a Category"""
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerial


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    """Endpoint to GET/PUT/PATCH/DELETE a Category ID"""
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerial

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Category Deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def categories_has_videos(request):
    """Endpoint to see Categories and its Videos"""
    category = Category.objects.all()
    serializer = PlaylistSerial(category, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def video_category_detail(request, pk):
    """Endpoint to see Videos by Category"""
    category = Category.objects.get(pk=pk)
    video = Video.objects.filter(category=category)
    serializer = VideoSerial(video, many=True)
    return Response(serializer.data) if len(video) > 0 else Response("No Videos in this Category",
                                                                     status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validate_token(request):
    """Endpoint to validate Token"""
    return Response("Token Validated")
