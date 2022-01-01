from django.urls import path
from . import views

urlpatterns = [
    path('materiels/', views.goMateriels,name='materiels'),
    path('createMateriel/', views.createMateriel,name='createMateriel'),
]
