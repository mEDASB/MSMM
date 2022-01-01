from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import User , Group



def create_profile(sender , instance , created ,**kwargs):
    if created:
        who = kwargs
        print(kwargs)
        # groupME = Group.objects.get(name='ME')
        # groupSTE = Group.objects.get(name='STE')
        # if
        # instance.groups.add(group)

        # Author.objects.create(
        #     user = instance,
        #     name = instance.username,
        #     email = instance.email
        # )

        # print("Author created successfully")


post_save.connect(create_profile,sender=User)