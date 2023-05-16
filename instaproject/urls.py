from django.contrib import admin
from django.urls import path
from instaapp import views
from instaapp.views import upload_photo
from django.conf import settings
from django.conf.urls.static import static
from instaapp.views import photo_grid


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('grid/', photo_grid, name='photo_grid'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
