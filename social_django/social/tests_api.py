import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from social.models import Post

@pytest.mark.django_db
def test_posts_with_token():
    user = User.objects.create_user(username='testuser', password='password123')
    token, _ = Token.objects.get_or_create(user=user)
    
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.get('/api/v1/posteo/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve_specific_post():

    user = User.objects.create_user(username='testuser', password='password123')
    token, _ = Token.objects.get_or_create(user=user)

  
    post = Post.objects.create(
        user=user,
        content="Este es un contenido de prueba"
      
    )

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


    response = client.get(f'/api/v1/posteo/{post.id}/')

    assert response.status_code == 200  


@pytest.mark.django_db
def test_creating_post_with_token():
    user = User.objects.create_user(username='testuser', password='password123')
    token, _ = Token.objects.get_or_create(user=user)
    
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

  
    post_data = {
        "content": "Contenido del nuevo post",
        "user": user.id,
    
    }

    response = client.post('/api/v1/posteo/', post_data, format='json')

    assert response.status_code == 201  

