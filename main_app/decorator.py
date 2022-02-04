
from django.shortcuts import redirect, render

from django import template
from django.contrib.auth.models import Group 
from .models import *





def unllowUsers():
    def decorator(viewfunc):
        def wrapper_func(request,*args, **kwargs):
            logs = Log.objects.all()
            logs_count = []
            for item in logs:
                if item.user == request.user:
                    logs_count.append(item)
            group=request.user.groups.all()[0].name
            if len(logs_count) == 1 :
                if group == 'ME':
                    return redirect('editInfoME')
                elif group == 'STE':
                    return redirect('editInfo')
            elif len(logs_count) > 1 :
                return redirect('posts')
        return wrapper_func
    return decorator





