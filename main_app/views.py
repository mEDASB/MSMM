from django.shortcuts import render , redirect


from .creation_forms import registerForm , ContactForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import Group
from me.models import *
from ste.models import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib import messages



# Create your views here.

def goHome(request):
    context = {}
    return render(request,'home.html',context)



def goDownload(request):
    context = {}
    return render(request,'download.html',context)




    
def goRegister(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        form = registerForm()
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                recaptcha_response = request.POST.get("g-recaptcha-response")
                data = {
                    'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response':recaptcha_response
                }
                rJson = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                result = rJson.json()
                if result["success"]:
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
                else:
                    messages.error(request,"please check i'm not a robot")
            
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
                recaptcha_response = request.POST.get("g-recaptcha-response")
                data = {
                    'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response':recaptcha_response
                }
                rJson = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                result = rJson.json()
                if result["success"]:
                    login(request,user)
                    group = user.groups.all()[0].name
                    Log.objects.create(
                        user=request.user
                    )
                    logs = Log.objects.all()
                    logs_count = []
                    for item in logs:
                        if item.user == request.user:
                            logs_count.append(item)
                    if group == 'ME':
                        if len(logs_count) == 1 :
                            return redirect('editInfoME')
                        elif len(logs_count) > 1 :
                            return redirect('me_myprofile')
                    elif group == 'STE':
                        if len(logs_count) == 1 :
                            return redirect('editInfoSTE')
                        elif len(logs_count) > 1 :
                            return redirect('ste_myprofile')
                
        context = {
            # 'group':group,
        }
        return render(request,'Auth/login.html',context)




def goLogout(request):
    logout(request)
    return redirect('login')





def goContact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                subject = "MSMM Messages" 
                body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email'], 
                'message':form.cleaned_data['message'], 
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, form.cleaned_data['email'], ['smcor64@gmail.com']) 
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect ("home")  
        form = ContactForm()
        context = {
            'form':form,
        }
        return render(request,'contact_us.html',context)