from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from social.models import Comment
from social.api.serializers import CommentSerializer


class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        comment_serializer = CommentSerializer(comments, many=True)
        return Response(comment_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response({'message': 'Comentario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDetailAPIView(APIView):
    def get(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data)

    def put(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        comment_serializer = CommentSerializer(comment, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        if comment:
            comment.delete()
            return Response('Comentario eliminado')
        return Response({'message': 'No se ha encontrado un comentario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
