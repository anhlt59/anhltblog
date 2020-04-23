from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime

from users.forms import UserLoginForm


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # import pdb; pdb.set_trace()
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            # authenticate check username password incorect
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    # saves the user’s ID in the session, using Django’s session framework
                    login(request, user)
                    return redirect(reverse_lazy("blog:post_list"))
                else:
                    return HttpResponse("user is not active")
            else:
                return HttpResponse("user is none")
    else:
        form = UserLoginForm()
    context = {
        "form": form,
    }
    return render(request, "registration/login.html", context)


def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("blog:post_list"))


def user_signup(request):
    return HttpResponse("register new user")


def user_reset(request):
    return HttpResponse("reset password")


def user_change_password(request):
    return HttpResponse("change password")


def user_profile(request):
    return HttpResponse("profile user")
