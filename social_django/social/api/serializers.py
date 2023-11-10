from rest_framework import serializers
from social.models import Profile, Post, Category, Comment


class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()  # campo imagen para manejar el modelo profile

    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id','name')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class TestPostSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()

    def validate_name(self,value):
        # custom validation
        if 'developer' in value:
            raise serializers.ValidationError('Error,no puede existir un usuario con ese nombre')
        
        return value

    def validate_email(self,value):
        if value == '':
            raise serializers.ValidationError('Tiene que indicar un correo')
        
        if self.validate_name(self.context['name']) in value:
                raise serializers.ValidationError('El email no puede contener el nombre')
            

        return value

    def validate(self,data):
    
        return data
        

# class PublicPostSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField()

#     class Meta:
#         model = Post
#         fields = ('id','author','title','content','image','category','tags','created_at','updated_at','slug')