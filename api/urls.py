from django.urls import include, path

from . import views

app_name = "api"

urlpatterns = [
    path("auth/register", views.CreateUserView.as_view(), name="register"),
    path("auth/", include("djoser.urls.authtoken")),
]
