from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    first_name = models.CharField(max_length = 50, null=False)
    last_name = models.CharField(max_length = 50, null=False)
    email = models.EmailField(max_length = 150, null=False)
    message = models.TextField(max_length = 2000,null=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['email'] 

    def __str__(self):
        return self.email





class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at'] 

    def __str__(self):
        return self.created_at