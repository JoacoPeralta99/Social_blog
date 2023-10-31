from django.urls import path
from .api import UserApiView

urlpatterns = [
    path('usuario/',UserApiView.as_view(),name = 'usuario_api')

]