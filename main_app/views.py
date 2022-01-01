from django.shortcuts import render , redirect


from .creation_forms import registerForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import Group
from me.models import *
from ste.models import *


# Create your views here.

def goHome(request):
    context = {}
    return render(request,'home.html',context)



def goDownload(request):
    context = {}
    return render(request,'home.html',context)



def goAbout(request):
    context = {}
    return render(request,'home.html',context)



    
def goRegister(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        form = registerForm()
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                user = form.save()
                groupME = Group.objects.get(name='ME')
                groupSTE = Group.objects.get(name='STE')
                who = request.POST.get('who')
                if who == "ME":

                    ME.objects.create(
                        user = user,
                        full_Name = user.username
                    )
                    user.groups.add(groupME)
                elif who == 'STE':
                    Societe.objects.create(
                        user = user,
                        name_STE = user.username
                    )
                    user.groups.add(groupSTE)
                print("create successfully !!!!!")
                return redirect('login')
            
        context = {
            'form':form
        }
        return render(request,'Auth/register.html',context)



def goLogin(request): 
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                group = user.groups.all()[0].name
                if group == 'ME':
                    return redirect('me_myprofile')
                elif group == 'STE':
                    return redirect('ste_myprofile')
                
        context = {
            # 'group':group,
        }
        return render(request,'Auth/login.html',context)




def goLogout(request):
    logout(request)
    return redirect('login')
