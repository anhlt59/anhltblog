from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib import messages
from datetime import datetime

from users.forms import UserLoginForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "registration/login.html"

    # def form_valid(self, form):
    #     messges.success(self.request, "Login success")
    #     return super().form_valid(form)


class LoginView(View):
    def get(self, request):
        return render(request, 'survey/login.html', { 'form':  AuthenticationForm })

    # really low level
    def post(self, request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is None:
                return render(
                    request,
                    'survey/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'survey/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)
            return redirect(reverse('profile'))

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
                    messages.success(request, f"Hi {user.username}")
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
