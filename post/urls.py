from django.urls import path
from . import views

urlpatterns = [
    path('', views.goHome,name='home'),
]
