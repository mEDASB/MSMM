
from django.shortcuts import redirect, render

from django import template
from django.contrib.auth.models import Group 
from .models import *





def Completig_Infos():
    def decorator(viewfunc):
        def wrapper_func(request,*args, **kwargs):

            group=request.user.groups.all()[0].name
            if group == 'ME':
                if request.user.me.is_completed == False:
                    return redirect('editInfoME')
            elif group == 'STE':
                if request.user.societe.is_completed == False:
                    return redirect('editInfoSTE')
            
            return viewfunc(request,*args, **kwargs)
        return wrapper_func
    return decorator





