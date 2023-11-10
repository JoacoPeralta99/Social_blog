from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from social.models import Profile
from social.api.serializers import ProfileSerializer, TestPostSerializer


class ProfileAPIView(APIView):
    def get(self, request):
        users = Profile.objects.all()
        users_serializer = ProfileSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = ProfileSerializer(data=request.data) # deserializacion se vuelve de json a objeto en base al modelo
        if user_serializer.is_valid():  # validacion del serializer
            user_serializer.save()
            return Response({'message': 'Perfil de usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailAPIView(APIView):
    def get(self, request, pk):
        user = Profile.objects.filter(id=pk).first()
        user_serializer = ProfileSerializer(user)
        return Response(user_serializer.data)

    def put(self, request, pk):
        user = Profile.objects.filter(id=pk).first()
        user_serializer = ProfileSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = Profile.objects.filter(id=pk).first()
        if user:
            user.delete()
            return Response('Perfil Eliminado')
        return Response({'message': 'No se ha encontrado un Perfil con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileTestAPIView(APIView):
    def post(self, request):
        test_data = {
            'name': 'pepito',
            'email': 'pepito@gmail.com',
        }
        test_post = TestPostSerializer(data=test_data, context=test_data)
        if test_post.is_valid():
            return Response({'message': 'Paso validaciones'}, status=status.HTTP_200_OK)
        return Response(test_post.errors, status=status.HTTP_400_BAD_REQUEST)