from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# start Societé Model

class Societe(models.Model):

   phone = models.CharField(max_length=14,null=False)
   villes = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   ville = models.CharField(max_length=100,null=False,choices=villes)
   photo = models.ImageField(blank=True,null=True,default="profile.png")
   created_at = models.DateTimeField(auto_now_add=True)
   name_STE = models.CharField(unique=True,max_length=50,null=False)
   web_Site = models.CharField(max_length=50,null=True)
   desc = models.TextField(null=True)
   cp_proof = models.ImageField(null=False)
   active = models.BooleanField(null=True,default=False)
   is_completed = models.BooleanField(null=True,default=False)
   DOMAINES = (
      ('in progress','in progress'),
      ('out the order','out the order'),
      ('Delivered','Delivered'),
      ('Pending','Pending')
   )
   domaine = models.CharField(max_length=100,null=False,choices=DOMAINES)
   user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

   def __str__(self):
      return self.name_STE
   def get_year(self):
      return self.created_at.year
