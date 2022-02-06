from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# start M'E Model

class ME(models.Model):
   phone = models.CharField(max_length=14,null=True)
   villes = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   ville = models.CharField(max_length=100,null=True,choices=villes)
   photo = models.ImageField(blank=True,null=True,default="profile.png")
   created_at = models.DateTimeField(auto_now_add=True)
   full_Name = models.CharField(max_length=50,null=True)
   CIN = models.CharField(max_length=10,null=True)
   cp_CIN = models.ImageField(null=True)
   Busy = models.BooleanField(null=True,default=False)
   active = models.BooleanField(null=True,default=False)
   is_completed = models.BooleanField(null=True,default=False)
   DOMAINES = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   domaine = models.CharField(max_length=100,null=True,choices=DOMAINES)
   user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

   def __str__(self):
      return self.full_Name

   
   def get_year(self):
      return self.created_at.year