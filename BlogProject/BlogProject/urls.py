"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from register import views as v

#Putting all the paths to the web application together
urlpatterns = [
    path('register/', v.register, name='register'), #allows access to the registration page
    path('admin/', admin.site.urls), #allows access to the admin page
    path('', include('articles.urls')), #includes all the paths in the articles folder from urls.py
    path('summernote/', include('django_summernote.urls')), #allows the text editor to display
    path('', include("django.contrib.auth.urls")), #allows the use of the default user auth in Django
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)