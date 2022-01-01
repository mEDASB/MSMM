from django.shortcuts import render,redirect
from .forms import profileForm
from .models import ME
from django.core.paginator import Paginator
from .filter import filterMe
from django.contrib.auth.decorators import login_required
from .decorator import allowUsers
# Create your views here.




@login_required(login_url='login')
@allowUsers(AllowGroups=['STE'])
def goMes(request):
    # All
    mes = ME.objects.all()
    paginatorAll = Paginator(mes, 5) 
    page_numberAll = request.GET.get('page')
    page_objAll = paginatorAll.get_page(page_numberAll)

    filter_Me = filterMe(request.GET,queryset=mes)
    page_objAll = filter_Me.qs

    context = {
        'page_objAll':page_objAll,
        'filter_Me':filter_Me,
    }
    return render(request,'mes.html',context)


@login_required(login_url='login')
def goProfile(request,pk):
    me = ME.objects.get(id=pk)
    context = {
        'me':me,
    }
    return render(request,'p_ME.html',context)


@login_required(login_url='login')
def ME_MyProfile(request):
    me = request.user.me
    context = {
        'me':me,
    }
    return render(request,'p_ME.html',context)



@login_required(login_url='login')
def editInfo(request):
    me = request.user.me
    form = profileForm(instance=me)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=me)
        if form.is_valid():
            form.save()
            return redirect('me_myprofile')
    context = {
        'form':form,
    }
    return render(request,'editInfo.html',context)

