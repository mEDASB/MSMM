from django.shortcuts import render


from ste.models import Societe
from me.models import ME


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



def goLogin(request):
    context = {}
    return render(request,'home.html',context)


    
def goRegister(request):
    context = {}
    return render(request,'home.html',context)

