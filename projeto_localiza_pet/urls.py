from django.contrib import admin
from django.urls import path
from app_localiza_pet import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # url da primeira pagina de login
    path('', views.entrada, name='entrada'),
    path('login/', views.login, name='login'),
    path('feed/', views.feed, name='feed'),
    path('post/', views.post, name='post'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout),
    path('post/', views.post, name='post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
