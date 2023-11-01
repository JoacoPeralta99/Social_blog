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
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    
#ejemplos para nuevos endpoints futuros 
# @api_view(['POST'])
# def create_profile(request):
#     if request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','POST'])
# def create_post(request):
#     if request.method == 'GET':
#         users = Post.objects.all()
#         users_Serializer = ProfileSerializer(users,many = True)
#         return Response(users_Serializer.data)    
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
