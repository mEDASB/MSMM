from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from django.core.cache import cache

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    print("user logged in successfully")

@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    print("user logged out successfully")
    # Clear cache
    cache.clear()







# from django.db.models.signals import post_save
# from .models import *
# from django.contrib.auth.models import User , Group
# def logout_user(sender , instance , request ,**kwargs):
#     if request.user.is_authenticated():

#         print("Author loged in successfully")


# post_save.connect(logout_user,sender=User)