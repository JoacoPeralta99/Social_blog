from rest_framework import viewsets,permissions,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from social.models import Post
from social.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
   
class PostDetailViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
 