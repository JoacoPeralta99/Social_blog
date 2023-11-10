from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from social.models import Comment
from social.api.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
