from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.conf import settings
from django.utils import timezone

def post_home(request):
    return HttpResponse("<h1> Hello</h1>")
    
# def post_create(request):
#     return HttpResponse("<h1> Create </h1>")
def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit = False)
        post.author = request.user
        post.save()
        messages.success(request, "Successfully Created!")
        return redirect("posts:list")
    context = {
    "title": "Create",
    "form": form,
    }
    return render(request, 'post_create.html', context)

# def post_detail(request):
#     return HttpResponse("<h1> Detail </h1>")
def post_detail(request, post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    if instance.publish>timezone.now().date() or instance .draft:
        if not (request.user.is_staff or request.user.is_superuser):
            raise Http404
    context = {
    "title": "Detail",
    "instance": instance,
    "share_string": quote(instance.content)
    }
    return render(request, 'post_detail.html', context)

def post_update(request, post_slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    instance = get_object_or_404(Post, slug=post_slug)
    form = PostForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Edited!")
        return redirect(instance.get_absolute_url())
    context = {
    "form":form,
    "instance": instance,
    "title": "Update",
    }
    return render(request, 'post_update.html', context)

def post_delete(request, post_slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    instance = get_object_or_404(Post, slug=post_slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:list")

# def post_list(request):
#     return HttpResponse("<h1> List </h1>")
def post_list(request):
    today = timezone.now().date()
    object_list = Post.objects.filter(draft=False).filter(publish__lte=today)
    if request.user.is_staff or request.user.is_superuser:
        object_list = Post.objects.all()

    paginator = Paginator(object_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    context = {
    "object_list": objects,
    "title": "List",
    "user": request.user,
    "today": today
    }
    return render(request, 'post_list.html', context)
    

     