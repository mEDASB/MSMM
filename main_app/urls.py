from django.urls import path
from . import views

urlpatterns = [
    path('', views.goHome,name='home'),
    path('download_app/', views.goDownload,name='download'),
    path('about_us/', views.goAbout,name='about_us'),

    # Auth Links
    path('login/', views.goLogin,name='login'),
    path('register/', views.goRegister,name='register'),
    path('logout/', views.goLogout,name='logout'),

    # functions process
    # path('choose_group', views.chooseGroup,name='choose'),
]
