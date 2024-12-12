from django.urls import path

from CRED_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index', views.index, name="index")
]