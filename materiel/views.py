from django.shortcuts import render , redirect
from .models import Material
from django.core.paginator import Paginator
from .forms import Materiel_Creation_Form
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def goMateriels(request):
    materiels = Material.objects.all()
    paginatorAll = Paginator(materiels,5)
    page_numberAll = request.GET.get('page')
    page_objAll = paginatorAll.get_page(page_numberAll)

    context = {
        'page_objAll':page_objAll,

    }
    return render(request,'materiels.html',context)


@login_required(login_url='login')
def createMateriel(request):
    form = Materiel_Creation_Form()
    if request.method == 'POST':
        form = Materiel_Creation_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Materiel created successfully")
            return redirect('materiels')
    context = {
        'form':form,
    }
    return render(request,'materiels_creation.html',context)