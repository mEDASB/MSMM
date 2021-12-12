from django.db import models

from ste.models import Societe
from me.models import ME

# Create your models here.



   
# start Payment Model

class Payment(models.Model):
   date_Payment = models.DateTimeField(auto_now_add=True)
   method_Payment = models.EmailField(max_length=254,null=False)
   ste = models.ForeignKey(Societe, on_delete=models.CASCADE)