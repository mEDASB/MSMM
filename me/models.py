from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# start M'E Model

class ME(models.Model):
   phone = models.CharField(max_length=14,null=False)
   villes = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   ville = models.CharField(max_length=100,null=False,choices=villes)
   photo = models.ImageField(blank=True,null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   full_Name = models.CharField(max_length=50,null=False)
   CIN = models.CharField(max_length=10,null=False)
   cp_CIN = models.ImageField(null=False)
   Busy = models.BooleanField(null=True,default=False)
   active = models.BooleanField(null=False)
   DOMAINES = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   domaine = models.CharField(max_length=100,null=False,choices=DOMAINES)
   user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

   def __str__(self):
      return self.CIN