
from django.forms.models import ModelForm
from .models import Material

class Materiel_Creation_Form(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        # exclude = ['user']
