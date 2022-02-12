from django.shortcuts import render,redirect
from .models import *
from me.models import ME
from .forms import create_post_form

from post.models import Post
from django.core.paginator import Paginator
from .filter import filterSte
from django.views.decorators.cache import cache_control

from django.contrib.auth.decorators import login_required
from main_app.decorator import Completig_Infos
import datetime
# Create your views here.


@login_required(login_url='login')
@Completig_Infos()
@cache_control(no_cache=True, must_revalidate=True)
def goPosts(request):
    # All
    posts = Post.objects.all()

    current_datetime = datetime.datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day
    for item in posts:
        i_year = item.date_experation.year
        i_month = item.date_experation.month
        i_day = item.date_experation.day
        if (i_year <= year) and (i_month <= month) and (i_day <= day):
            item.expiration = True
            item.save()

    posts_not_Exp = Post.objects.filter(expiration = False)

    filter_Ste = filterSte(request.GET,queryset=posts_not_Exp)
    page_objAll = filter_Ste.qs

    paginator = Paginator(page_objAll, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj':page_obj,
        'filter_Ste':filter_Ste,
    }
    return render(request,'posts.html',context)



@login_required(login_url='login')
@Completig_Infos()
def goPost(request,pk):
    var = 0 
    post = Post.objects.get(id=pk)
    
    group=request.user.groups.all()[0].name
    if group == "ME":
        me = request.user.me
        me_post_s = MePost.objects.all()
        m_p_s = me_post_s.filter(post = post)
        for item in m_p_s:
            if item.me == me:
                var = 1
    elif group == "STE":
        ste = request.user.societe
        if post.ste == ste:
            var = 2

    try:

        ste = request.user.societe
    except:
        
        ste = post.ste

    # me for this post

    me_post = MePost.objects.all().filter(post= post)
    # mes = ME.objects.all().filter(me = me_post.me)


    context = {
        'post':post,
        'var':var,
        'ste':ste,
        'mes':me_post,
    }
    return render(request,'post.html',context)




@login_required(login_url='login')
def addRequest(request,pk):
    me = ME.objects.get(id=request.user.me.id)
    post = Post.objects.get(id=pk)
    post.count_Dommand += 1
    post.save()
    me_post = MePost.objects.create(
        me = me,
        post = post,

    )
    print("Demmand created successfully")
    return redirect('post',post.id)




@login_required(login_url='login')
def unRequest(request,pk):

    me = ME.objects.get(id=request.user.me.id)
    post = Post.objects.get(id=pk)
    post.count_Dommand -= 1
    post.save()
    me_post = MePost.objects.all().filter(me=me)
    mp = me_post.filter(post = post)
    mp.delete()
    print("Demmand deleted successfully")
    return redirect('post',post.id)


@login_required(login_url='login')
@Completig_Infos()
def Create(request):
    form = create_post_form()
    if request.method == 'POST':
        form = create_post_form(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            post.ste = request.user.societe
            post.save()
            print("created successfully")
            return redirect('posts')
    context = {
        'form':form,
    }
    return render(request,'create_post.html',context)



@login_required(login_url='login')
def UPdate(request,pk):
    post = Post.objects.get(id=pk)
    form = create_post_form(instance = post)
    if request.method == 'POST':
        form = create_post_form(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            print("created successfully")
            return redirect('posts')
    context = {
        'form':form,
    }
    return render(request,'create_post.html',context)


@login_required(login_url='login')
def Delete(request,pk):

    post = Post.objects.get(id=pk)

    if request.method == 'POST':
            post.delete()
            return redirect('posts')

    return render(request,'delete_confirmation.html')