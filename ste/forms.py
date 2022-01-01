


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Societe


class profileForm(ModelForm):
    class Meta:
        model = Societe
        fields = '__all__'
        exclude = ['user']
