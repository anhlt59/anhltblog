from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime

from blog.forms import PostCreateForm
from blog.models import Post

# Create your views here.


def index(request):
    return redirect("blog:post_list")


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, slug, id):
    # try:
    #     post = Post.objects.get(slug=slug, id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    # or using get_object_or_404
    post = get_object_or_404(Post, id=id, slug=slug)
    context = {
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)


@login_required
def mypost_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()

    context = {
        "form": form,
    }
    return render(request, "blog/post_create.html", context)


@login_required
def mypost_list(request):
    author = request.user.username
    posts = Post.objects.filter(author__username=author).all()
    context = {
        "posts": posts,
        "admin": True,
        "title": f"{author}'s Posts",
    }
    return render(request, "blog/post_list.html", context)


@login_required
def mypost_delete(request):
    if request.method == "POST":
        author = request.user.username
        username = request.POST.get("username")
        id = request.POST.get("id")

        if author == username:
            Post.objects.filter(id=id).delete()

    posts = Post.objects.filter(author=author).all()
    context = {
        "posts": posts,
        "admin": True
    }
    return redirect(request, "blog/post_delete.html", context)


@login_required
def mypost_edit(request):
    return HttpResponse('mypost_edit')
