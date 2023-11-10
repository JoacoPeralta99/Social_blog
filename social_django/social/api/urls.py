from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken 
from .views.profile_views import ProfileViewSet, ProfileDetailViewSet
from .views.category_views import CategoryViewSet, CategoryDetailViewSet
from .views.post_views import PostViewSet, PostDetailViewSet
from .views.comment_views import CommentViewSet, CommentDetailViewSet

router = DefaultRouter()
router.register(r'perfil', ProfileViewSet, basename='perfil-api')
router.register(r'perfil-detalle', ProfileDetailViewSet, basename='perfil-detalle-api')
router.register(r'categoria', CategoryViewSet, basename='categoria-api')
router.register(r'categoria-detalle', CategoryDetailViewSet, basename='categoria-detalle-api')
router.register(r'posteo', PostViewSet, basename='posteo-api')
router.register(r'posteo-detalle', PostDetailViewSet, basename='posteo-detalle-api')
router.register(r'comentarios', CommentViewSet, basename='commentario-api')
router.register(r'comentarios-detalle', CommentDetailViewSet, basename='commentario-detalle-api')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', ObtainAuthToken.as_view(), name = 'token-api')
]
