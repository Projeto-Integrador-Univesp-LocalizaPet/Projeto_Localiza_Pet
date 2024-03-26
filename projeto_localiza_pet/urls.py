# from django.contrib import admin

from django.urls import path

from app_localiza_pet import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # url da primeira pagina de login
    path('', views.home, name='home'),

]
