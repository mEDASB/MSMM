from .models import *
import django_filters




class filterMe(django_filters.FilterSet):
    class Meta:
        model =  ME
        fields = ['full_Name','ville']