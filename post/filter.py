from post.models import *
import django_filters
from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'

class filterSte(django_filters.FilterSet):
    create_at = django_filters.DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )

    class Meta:
        model =  Post
        fields = ['create_at'] 