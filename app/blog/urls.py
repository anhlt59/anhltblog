from django.urls import path
from blog import views


app_name = "blog"
urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<slug:slug>_<int:id>", views.PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>_<int:id>/edit", views.mypost_edit, name="mypost_edit"),
    path("<slug:slug>_<int:id>/delete", views.mypost_delete, name="mypost_delete"),
    path("mypost_create", views.MypostCreateView.as_view(), name="mypost_create"),
    path("mypost_list", views.MypageListView.as_view(), name="mypost_list"),
]
