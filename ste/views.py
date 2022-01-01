from django.shortcuts import render , redirect
from .forms import profileForm
from .models import Societe
from django.core.paginator import Paginator
from .filter import filterSte
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
# Create your views here.




@login_required(login_url='login')
def goSTE(request):
    # All
    societes = Societe.objects.all()
    paginatorAll = Paginator(societes, 5) 
    page_numberAll = request.GET.get('page')
    page_objAll = paginatorAll.get_page(page_numberAll)

    filter_Ste = filterSte(request.GET,queryset=societes)
    page_objAll = filter_Ste.qs

    context = {
        'page_objAll':page_objAll,
        'filter_Ste':filter_Ste,
    }
    return render(request,'societes.html',context)


@login_required(login_url='login')
def goProfile(request,pk):
    ste = Societe.objects.get(id=pk)
    context = {
        'ste':ste,
    }
    return render(request,'p_STE.html',context)



@login_required(login_url='login')
def MyProfile(request):
    ste = request.user.societe
    context = {
        'ste':ste,
    }
    return render(request,'p_STE.html',context)


@login_required(login_url='login')
def editInfo(request):
    ste = request.user.societe
    form = profileForm(instance=ste)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=ste)
        if form.is_valid():
            form.save()
            return redirect('ste_myprofile')
    context = {
        'form':form,
    }
    return render(request,'editInfo.html',context)

