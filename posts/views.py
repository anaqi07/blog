from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404

def post_home(request):
    return HttpResponse("<h1> Hello</h1>")
    
# def post_create(request):
#     return HttpResponse("<h1> Create </h1>")
def post_create(request):
    return render(request, 'post_create.html', {})

# def post_detail(request):
#     return HttpResponse("<h1> Detail </h1>")
def post_detail(request):
    instance = instance = get_object_or_404(Post, id=1)
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
def post_update(request):
    return render(request, 'post_update.html', {})
    
# def post_delete(request):
#     return HttpResponse("<h1> Delete </h1>")
def post_delete(request):
    return render(request, 'post_delete.html', {})
     