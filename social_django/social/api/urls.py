from django.urls import path
from .views.api import user_api_view,create_profile,create_post

urlpatterns = [
    path('usuario/',user_api_view,name = 'usuario_api'),
    path('api/create_profile/', create_profile, name='create_profile'),
    path('api/create_post/', create_post, name='create_post'),
]