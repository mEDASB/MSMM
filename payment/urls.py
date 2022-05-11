from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.goOffers,name='offers'),
    path('choose_offer/<str:amount>', views.goChoose_offer,name='choose_offer'),
    # path('charge/', views.goCharge,name='charge'),
    # path('success/<str:args>', views.goOffers,name='offers'),
]
