from .models import *
import django_filters




class FilterMateriel(django_filters.FilterSet):
    class Meta:
        model =  Material
        fields = ['Libell','Categorie','prix']