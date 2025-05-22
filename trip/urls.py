from django.contrib import admin
from django.urls import path
from owner import views
from trip import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/',views.index),
    # path('insertuser/',views.insertuser),
    # path('login/',views.login),
    path('tripplan/',views.insert_trip)
    
]