from django.db import models


from ste.models import Societe
from me.models import ME

# Create your models here.


# start Post Model

class Post(models.Model):
   title = models.CharField(max_length=200,null=True)
   Description = models.TextField(null=True)
   date_experation = models.DateField(null=True)
   create_at = models.DateField(auto_now_add=True,null=True)
   photo = models.ImageField(null=False)
   count_Dommand = models.IntegerField(null=True,default=0)
   me = models.ManyToManyField(ME,through='MePost')
   ste = models.ForeignKey(Societe, on_delete=models.CASCADE,null=True)
   expiration = models.BooleanField(null=True,default=False)

   class Meta:
        ordering = ['create_at'] 

   def __str__(self):
      return self.title

class MePost(models.Model):
    date_Demmand = models.DateField(auto_now_add=True)
    me = models.ForeignKey(ME, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
