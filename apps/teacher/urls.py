from django.urls import path

from .views import RegisterView, ProfileView, SignIn


urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", SignIn.as_view(), name="login")
]