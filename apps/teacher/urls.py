from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import RegisterView, ProfileView, SignIn

app_name = 'teacher'

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", SignIn.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]