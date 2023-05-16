from django.contrib import admin
from django.urls import path, include
from instaapp import views
from django.conf import settings
from django.conf.urls.static import static
from instaapp.views import ProfileView
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from instaapp.views import create_comment
from instaapp.views import ProfileView



urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('grid/', views.photo_grid, name='photo_grid'),
    path('create_post/', views.create_post_link, name='create_post_link'),
    path('home/', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),  # Add this line for the /accounts/profile/ URL
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/user/<int:user_id>/', views.get_user_profile, name='get_user_profile'),
    path('api/post/<int:post_id>/', views.get_post, name='get_post'),
    path('api/comment/<int:comment_id>/', views.get_comment, name='get_comment'),
    path('api/create_post/', views.create_post, name='create_post'),
    path('api/update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('api/delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment'),
    path('api/all_users/', views.get_all_users, name='get_all_users'),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('profile' if request.user.is_authenticated else 'login'), name='root'),
    path('signup/', views.register, name='signup'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('grid/', views.photo_grid, name='grid'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
