from django.urls import path
from blog import views


app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<slug:slug>-<int:id>", views.post_detail, name="post_detail"),
    path("<slug:slug>-<int:id>/edit", views.mypost_edit, name="mypost_edit"),
    path("<slug:slug>-<int:id>/delete", views.mypost_delete, name="mypost_delete"),
    path("mypost_create", views.mypost_create, name="mypost_create"),
    path("mypost_list", views.mypost_list, name="mypost_list"),
]
