from django.shortcuts import render , redirect
from .forms import profileForm
from .models import Societe
from django.core.paginator import Paginator
from .filter import filterSte
from django.contrib.auth.decorators import login_required
from post.models import Post
@login_required(login_url='login')
# Create your views here.




@login_required(login_url='login')
def goSTE(request):
    # All
    societes = Societe.objects.all()
    filter_Ste = filterSte(request.GET,queryset=societes)
    page_objAll = filter_Ste.qs

    paginator = Paginator(page_objAll, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj':page_obj,
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
    
    form = profileForm(instance=ste)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=ste)
        if form.is_valid():
            form.save()
            return redirect('ste_myprofile')

    
    posts = Post.objects.all()
    posts_ste = []
    for item in posts:
        if item.ste == ste:
            posts_ste.append(item)

    context = {
        'ste':ste,
        'posts':posts_ste,
        'form':form,
    }
    return render(request,'my_p_STE.html',context)


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
    return render(request,'editInfoSTE.html',context)

