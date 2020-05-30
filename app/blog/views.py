from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from blog.forms import PostCreateForm
from blog.models import Post


class PostListView(ListView):
    paginate_by = 30
    template_name = "blog/post_list.html"
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.select_related("author").filter(status="published")
        return queryset


class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            Post.objects.select_related("author"),
            id=self.kwargs.get('id', None),
            slug=self.kwargs.get('slug', None)
        )
        return obj


class MypageListView(LoginRequiredMixin, ListView):
    paginate_by = 30
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    login_url = reverse_lazy('users:login')

    def handle_no_permission(self):
        messages.warning(self.request, "You need to login first")
        return super().handle_no_permission()

    def get_queryset(self):
        author = self.request.user.username
        queryset = Post.objects.filter(author__username=author).select_related("author")
        # message info your post
        # count = queryset.count()
        # if count:
        #     messages.success(self.request, f"You have {count} post")
        # else:
        #     try:
        #         messages.warning(self.request, "You have no post !")
        #     except Exception as e:
        #         print(e)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title=f"{self.request.user.username}'s Posts",
            admin=True
        )
        return context


class MypostCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog/post_create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:mypost_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, 'You post is created')
        return redirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update(author=self.request.user)
        return kwargs


class MypostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "blog/post_create.html"
    success_url = reverse_lazy('blog:mypost_list')
    model = Post


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

# def post_list(request):
#     posts = Post.objects.select_related("author").all()
#     context = {
#         "posts": posts,
#     }
#     return render(request, "blog/post_list.html", context)
# def post_detail(request, slug, id):
#     try:
#         post = Post.objects.select_related("author").get(slug=slug, id=id)
#     except Post.DoesNotExist:
#         raise Http404("Post does not exist")
#     # # or using get_object_or_404
#     # post = get_object_or_404(Post, id=id, slug=slug)
#     context = {
#         "post": post,
#     }
#     return render(request, "blog/post_detail.html", context)
# @login_required
# def mypost_create(request):
#     if request.method == "POST":
#         form = PostCreateForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#     else:
#         form = PostCreateForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "blog/post_create.html", context)
# @login_required
# def mypost_list(request):
#     author = request.user.username
#     posts = Post.objects.filter(author__username=author).all()
#     context = {
#         "posts": posts,
#         "admin": True,
#         "title": f"{author}'s Posts",
#     }
#     return render(request, "blog/post_list.html", context)
# @login_required
# def mypost_delete(request):
#     if request.method == "POST":
#         author = request.user.username
#         username = request.POST.get("username")
#         id = request.POST.get("id")
#         if author == username:
#             Post.objects.filter(id=id).delete()
#     posts = Post.objects.filter(author=author).all()
#     context = {
#         "posts": posts,
#         "admin": True
#     }
#     return redirect(request, "blog/post_delete.html", context)
# @login_required
# def mypost_edit(request):
#     return HttpResponse('mypost_edit')