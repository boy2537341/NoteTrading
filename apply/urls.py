"""vh5000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('apply', views.apply, name='apply'),
    path('welcome/', views.welcome, name='welcome'),
    path('myapply/', views.myapply, name='my-apply'),
    path('persons/', views.all_person, name='persons'),
    path('updateperson/<int:id>', views.update_person, name='updateperson'),
]
