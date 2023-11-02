from rest_framework import serializers
from social.models import Profile, Post

class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()  # campo imagen para manejar el modelo profile
    class Meta:
        model = Profile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'