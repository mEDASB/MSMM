from django.urls import path
from . import views

urlpatterns = [    
    path('mes/', views.goMes,name='mes'),
    path('me_profile/<str:pk>', views.goProfile,name='me_profile'),
    path('me_myprofile/', views.ME_MyProfile,name='me_myprofile'),
    path('edit_info', views.editInfo,name='editInfo'),
]
