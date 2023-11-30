from django.urls import path

from social import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'blog'


urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    
    path('login/',LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('post/', views.post, name='post'),
    

    path('categories', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/detail', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', views.CreateCategoryView.as_view(), name='create_category'),
    path('categories/<int:category_id>/update/', views.UpdateCategoryView.as_view(), name='update_category'),
    path('categories/<int:category_id>/delete/', views.DeleteCategoryView.as_view(), name='delete_category'),

   
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # subir archivos estaticos por usuario

