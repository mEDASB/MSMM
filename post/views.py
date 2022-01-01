from django.shortcuts import render,redirect
from .models import *
from me.models import ME
from .forms import create_post_form

from post.models import Post
from django.core.paginator import Paginator
from .filter import filterSte

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def goPosts(request):
    # All
    posts = Post.objects.all()
    paginatorAll = Paginator(posts, 5) 
    page_numberAll = request.GET.get('page')
    page_objAll = paginatorAll.get_page(page_numberAll)

    filter_Ste = filterSte(request.GET,queryset=posts)
    page_objAll = filter_Ste.qs

    context = {
        'page_objAll':page_objAll,
        'filter_Ste':filter_Ste,
    }
    return render(request,'posts.html',context)



@login_required(login_url='login')
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


    context = {
        'post':post,
        'var':var,
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