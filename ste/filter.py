from .models import *
import django_filters
from django import forms




class filterSte(django_filters.FilterSet):

    class Meta:
        model =  Societe
        fields = ['name_STE','domaine'] 