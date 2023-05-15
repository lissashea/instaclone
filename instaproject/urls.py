from django.contrib import admin
from django.urls import path
from instaapp import views
from instaapp.views import upload_photo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('upload/', upload_photo, name='upload_photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
