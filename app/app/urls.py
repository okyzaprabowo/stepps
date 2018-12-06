"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('dashboard/', views.index, name='index'),
    path('sc/get/', views.result_sc, name='result_sc'),
    path('t/get/', views.result_t, name='result_t'),
    path('e/get/', views.result_e, name='result_e'),
    path('pu/get/', views.result_pu, name='result_pu'),
    path('pr/get/', views.result_pr, name='result_pr'),
    path('st/get/', views.result_st, name='result_st'),
]
