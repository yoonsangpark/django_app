from django.urls import path
from smartschool import views

urlpatterns = [
    path('', views.index),
]