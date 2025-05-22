"""
URL configuration for travellbuddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from owner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('insertuser/',views.insertuser),
    path('login/',views.login),
    path('trip/',views.insert_trip),
    path('findride/',views.search_trips),
    path('complaints/',views.submit_complaint,name='submit_complaint'),
    # path('submit_complaint/',views.submit_complaint)
]

