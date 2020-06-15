from django.urls import path
from . import views

app_name = 'caspian'
urlpatterns = [
    path('', views.index, name='index')
]
