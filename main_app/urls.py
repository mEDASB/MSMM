from django.urls import path
from . import views
from django.contrib.auth import views as Auth_Views

urlpatterns = [
    path('', views.goHome,name='home'),
    path('download_app/', views.goDownload,name='download'),
    path('contact_us/', views.goContact,name='contact_us'),

    # Auth Links
    path('login/', views.goLogin,name='login'),
    path('register/', views.goRegister,name='register'),
    path('logout/', views.goLogout,name='logout'),


    path('reset_password/', Auth_Views.PasswordResetView.as_view(template_name="Auth/password_reset.html"),name='reset_password'),
    path('reset_password_sent/', Auth_Views.PasswordResetDoneView.as_view(template_name="Auth/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', Auth_Views.PasswordResetConfirmView.as_view(template_name="Auth/password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/', Auth_Views.PasswordResetCompleteView.as_view(template_name="Auth/password_reset_done.html"),name='password_reset_complete'),


    
]
