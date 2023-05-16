from django.contrib import admin
from django.urls import path
from instaapp import views
from instaapp.views import upload_photo, login_view
from django.conf import settings
from django.conf.urls.static import static
from instaapp.views import photo_grid
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'), 
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('grid/', views.photo_grid, name='photo_grid'),  # Update the URL pattern for the grid to point to 'photo_grid' view
    path('create_post/', views.create_post_link, name='create_post_link'),
    path('api/user/<int:user_id>/', views.get_user_profile, name='get_user_profile'),
    path('api/post/<int:post_id>/', views.get_post, name='get_post'),
    path('api/comment/<int:comment_id>/', views.get_comment, name='get_comment'),
    path('api/create_post/', views.create_post, name='create_post'),
    path('api/update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('api/delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('api/all_users/', views.get_all_users, name='get_all_users'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
