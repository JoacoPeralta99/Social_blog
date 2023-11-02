from rest_framework.parsers import MultiPartParser, FormParser
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
        return Response(users_Serializer.data)    
    elif request.method == 'POST':
        user_serializer = ProfileSerializer(data = request.data) # deserializacion se vuelvo de json a objeto en base al modelo
        if user_serializer.is_valid():  # validacion del serializer
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)