from django.urls import path
from django.contrib.auth import views as auth_views
from users import views


app_name = "users"
urlpatterns = [
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("signup", views.user_signup, name="signup"),
    path("reset", views.user_reset, name="reset"),
    path("profile", views.user_profile, name="profile"),
    path("change_password", views.user_change_password, name="change_password"),

    # password reset url
    # path("password-reset", auth_views.password_reset, name="password_reset"),
    # path("password-reset/done/", auth_views.password_reset_done, name="password_reset_done"),
    # path("password-reset/confirm/<uuid:uuid>/<token:str>", auth_views.password_reset_confirm, name="password_reset_confirm"),
    # path("password-reset/complete/", auth_views.password_reset_complete, name="password_reset_complete"),
]
