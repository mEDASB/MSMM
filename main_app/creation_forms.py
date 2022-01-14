from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Message


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ['first_name','last_name','email','message']