
from django.shortcuts import redirect, render

def allowUsers(AllowGroups):
    def decorator(viewfunc):
        def wrapper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                if group in AllowGroups:
                    return viewfunc(request,*args, **kwargs)
                else:
                    return redirect('posts') 
        return wrapper_func
    return decorator