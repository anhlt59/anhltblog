from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    pass
    # def confirm_login_allowed(self, user):
    #     if not user.is_active or not user.is_validated:
    #         raise forms.ValidationError(
    #             'There was a problem with your login.',
    #             code='invalid_login'
    #         )
