from django.urls import path
from . import views

urlpatterns = [
    path('', views.goHome,name='home'),
    path('download_app/', views.goDownload,name='download'),
    path('contact_us/', views.goContact,name='contact_us'),

    # Auth Links
    path('login/', views.goLogin,name='login'),
    path('register/', views.goRegister,name='register'),
    path('logout/', views.goLogout,name='logout'),

    
]
