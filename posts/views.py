from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm

def post_home(request):
    return HttpResponse("<h1> Hello</h1>")
    
# def post_create(request):
#     return HttpResponse("<h1> Create </h1>")
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("posts:list")
    context = {
    "title": "Create",
    "form": form,
    }
    return render(request, 'post_create.html', context)

# def post_detail(request):
#     return HttpResponse("<h1> Detail </h1>")
def post_detail(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Detail",
    "instance": instance
    }
    return render(request, 'post_detail.html', context)

# def post_list(request):
#     return HttpResponse("<h1> List </h1>")
def post_list(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "List",
    "user": request.user
    }
    return render(request, 'post_list.html', context)

# def post_update(request):
#     return HttpResponse("<h1> Update </h1>")
def post_update(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect(instance.get_absolute_url())
    context = {
    "form":form,
    "instance": instance,
    "title": "Update",
    }
    return render(request, 'post_update.html', context)
    
# def post_delete(request):
#     return HttpResponse("<h1> Delete </h1>")
def post_delete(request):
    return render(request, 'post_delete.html', {})
     