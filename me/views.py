from django.shortcuts import render,redirect
from .forms import profileForm
from .models import ME
from django.core.paginator import Paginator
from .filter import filterMe
from django.contrib.auth.decorators import login_required
from .decorator import allowUsers
from main_app.decorator import Completig_Infos
# Create your views here.




@login_required(login_url='login')
@allowUsers(AllowGroups=['STE'])
@Completig_Infos()
def goMes(request):
    # All
    mes = ME.objects.all()
    filter_Me = filterMe(request.GET,queryset=mes)
    page_objAll = filter_Me.qs

    paginator = Paginator(page_objAll, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj':page_obj,
        'filter_Me':filter_Me,
    }
    return render(request,'mes.html',context)


@login_required(login_url='login')
@Completig_Infos()
def goProfile(request,pk):
    me = ME.objects.get(id=pk)
    
    context = {
        'me':me
    }
    return render(request,'p_ME.html',context)


@login_required(login_url='login')
@Completig_Infos()
def ME_MyProfile(request):
    me = request.user.me
    form = profileForm(instance=me)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=me)
        if form.is_valid():
            form.save()
            return redirect('me_myprofile')
    context = {
        'me':me,
        'form':form,
    }
    return render(request,'my_p_ME.html',context)



@login_required(login_url='login')
def editInfoME(request):
    me = request.user.me
    form = profileForm(instance=me)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=me)
        if form.is_valid():
            me = form.save()
            me.is_completed = True
            me.save()
            return redirect('me_myprofile')
    context = {
        'form':form,
    }
    return render(request,'editInfo.html',context)

