from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.goPosts,name='posts'),
    path('post/<str:pk>', views.goPost,name='post'),
    path('request/<str:pk>', views.addRequest,name='request'),
    path('unrequest/<str:pk>', views.unRequest,name='unrequest'),
    path('create/', views.Create,name='create'),
    path('update/<str:pk>', views.UPdate,name='update'),
    path('delete/<str:pk>', views.Delete,name='delete'),
]
