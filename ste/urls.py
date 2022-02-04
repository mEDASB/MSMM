from django.urls import path
from . import views

urlpatterns = [
    path('societes', views.goSTE,name='societes'),
    path('STE_profile/<str:pk>', views.goProfile,name='p_societe'),
    path('ste_myprofile/', views.MyProfile,name='ste_myprofile'),
    path('edit_info_STE', views.editInfo,name='editInfoSTE'),
]
