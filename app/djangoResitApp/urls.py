"""djangoResitApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path
from django.shortcuts import redirect
from django.conf.urls.static import static
from inWhite import views
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    path('', lambda request: redirect('properties'), name='home'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile', views.profile, name='profile'),
    path('login', views.LoginInterfaceView.as_view(), name="login"),
    path('logout', views.LogoutInterfaceView.as_view(), name="logout"),
    path("registration", views.registration_request, name="registration"),
    path('properties', views.properties, name='properties'),
    path('properties/<int:property_id>/', views.property_details, name='property_details'),
    path('search-results', views.PropertiesSearchView.as_view(), name="search_results"),
    #path('properties/create/', views.create.as_view(), name="create"),
    path('properties/create/', views.create, name="create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
