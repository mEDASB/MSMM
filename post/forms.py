
from django.forms.models import ModelForm
from .models import Post

# from bootstrap_datepicker_plus import DatePickerInput






class create_post_form(ModelForm):


    class Meta:
        model = Post
        fields = ['title','Description','date_experation','photo']
        exclude = ['Societe','ME']
        # widgets = {
        #     'date_experation':DatePickerInput(),
        # }
