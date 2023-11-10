from django.urls import path
from .views.profile_views import ProfileAPIView, ProfileDetailAPIView, ProfileTestAPIView
from .views.category_views import CategoryAPIView, CategoryDetailAPIView
from .views.post_views import PostAPIView, PostDetailAPIView
from .views.comment_views import CommentAPIView, CommentDetailAPIView

urlpatterns = [
    path('perfil/', ProfileAPIView.as_view(), name = 'perfil-api'),
    path('perfil/<int:pk>/', ProfileDetailAPIView.as_view(), name = 'perfil-detalle-api'),
    path('categoria/', CategoryAPIView.as_view(), name = 'categoria-api'),
    path('categoria/<int:pk>/', CategoryDetailAPIView.as_view(), name = 'categoria-detalle-api'),
    path('posteo/', PostAPIView.as_view(), name ='posteo-api'),
    path('posteo/<int:pk>/', PostDetailAPIView.as_view(), name ='posteo-detalle-api'),
    path('comentario/', CommentAPIView.as_view(), name='comentario-api'),
    path('comentario/<int:pk>/', CommentDetailAPIView.as_view(), name='detalle-comentario-api'),

]

