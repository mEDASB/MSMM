from django.db import models

from me.models import ME
from ste.models import Societe

# Create your models here.


# start Material Model

class Material(models.Model):
   name_Material = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   Libell = models.CharField(max_length=30,null=False,choices=name_Material)  
   create_at = models.DateTimeField(auto_now_add=True)
   prix = models.FloatField(null=False)
   # location => True , vendre => False
   VL = models.BooleanField(null=False)
   # not busy => True , busy => False
   # Busy = models.BooleanField(null=True,default=False)
   photo = models.ImageField(null=False)
   ste = models.ForeignKey(Societe, on_delete=models.CASCADE)
   me = models.ForeignKey(ME, on_delete=models.CASCADE)  
   CATEGORIE = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   Categorie = models.CharField(max_length=30,null=False,choices=CATEGORIE)  

   def __str__(self):
      return self.Libell
