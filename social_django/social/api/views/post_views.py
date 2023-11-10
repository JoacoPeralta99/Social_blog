from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from social.models import Post
from social.api.serializers import PostSerializer


class PostAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response({'message': 'Posteo creado correctamente!'}, status=status.HTTP_201_CREATED)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):

    def get(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)

    def put(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        post_serializer = PostSerializer(post, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.delete()
            return Response('Posteo eliminado')
        
        return Response({'message': 'No se ha encontrado un posteo con estos datos'}, status=status.HTTP_404_NOT_FOUND)
