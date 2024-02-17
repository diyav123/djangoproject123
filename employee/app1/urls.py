"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views
app_name="app1"

urlpatterns = [
    path('',views.view,name="view"),
    path('/add',views.add,name="add"),
    path('add1/<int:p>',views.add1,name="add1"),
    path('view1/<int:p>',views.view1,name="view1"),
    path('detail_delete/<int:p>',views.detail_delete,name="detail_delete"),
]
