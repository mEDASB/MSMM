from django.db import models

from django.contrib.auth.models import User

# Create your models here.



   
# start Payment Model

class Payment(models.Model):
   amount = models.IntegerField(null=False,default=0)
   count = models.IntegerField(null=True,default=0)
   date_Payment = models.DateTimeField(auto_now_add=True)
   user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)


   # def __str__(self):
   #    return self.count
   def get_year(self):
      return self.date_Payment.year