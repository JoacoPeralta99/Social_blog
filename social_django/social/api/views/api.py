from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from social.models import Profile,Post
from social.api.serializers import ProfileSerializer, PostSerializer

@api_view(['GET','POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = Profile.objects.all()
        users_Serializer = ProfileSerializer(users,many = True)
        return Response(users_Serializer.data, status = status.HTTP_200_OK)    
    elif request.method == 'POST':
        user_serializer = ProfileSerializer(data = request.data) # deserializacion se vuelve de json a objeto en base al modelo
        if user_serializer.is_valid():  # validacion del serializer
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk = None):

    if request.method == 'GET':
        user = Profile.objects.filter(id = pk).first()
        user_serializer = ProfileSerializer(user)
        return Response(user_serializer.data)
    
    elif request.method =='PUT':
        request.data
        user = Profile.objects.filter(id = pk).first()
        user_serializer = ProfileSerializer(user,data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user = Profile.objects.filter(id = pk).first()
        user.delete()
        return Response('Perfil Eliminado')