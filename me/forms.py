
from django.forms.models import ModelForm
from .models import ME


class profileForm(ModelForm):
    class Meta:
        model = ME
        fields = '__all__'
        exclude = ['user','is_completed']
