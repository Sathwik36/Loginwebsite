from django.contrib import admin
from django.urls import path
from homefirst import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('version',views.version,name="version"),
    path('services',views.services,name="services"),
    path('submit',views.sub,name="sub")
]