from rest_framework.response import Response
from rest_framework.views import APIView
from social.models import Profile
from social.api.serializers import UserSerializer

class UserApiView(APIView):

    def get(self,request):
        users = Profile.objects.all()
        users_Serializer = UserSerializer(users,many = True)
        return Response(users_Serializer.data)    