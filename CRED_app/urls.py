from django.urls import path

from CRED_app import views
from CRED_app.views import delete_data

urlpatterns = [
    path('',views.home,name="home"),
    path('index', views.index, name="index"),
    path('read',views.read, name="read"),

    path('delete_data/<int:id>/',views.delete_data,name='delete_data'),
    path('update_data/<int:id>/',views.update_data,name='update_data')
]