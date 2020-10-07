from django.urls import include, path, re_path

from . import views

app_name = "api"

urlpatterns = [
    path("auth/register", views.CreateUserView.as_view(), name="register"),
    path("auth/", include("djoser.urls.authtoken")),
    path("users/", views.UsersView.as_view(), name="users"),

    re_path(r"^posts/upload_image/(?P<filename>[^/]+)$", views.AddPostView.as_view(), name="posts_add_image"),
    path("posts/add_caption/<pk>", views.AddPostCaptionView.as_view(), name="posts_add_caption"),
    path("posts/like/<pk>", views.LikePostView.as_view(), name="posts_like"),
    path("posts/unlike/<pk>", views.UnlikePostView.as_view(), name="posts_unlike"),
    path("posts/", views.PostsListView.as_view(), name="posts"),
]
