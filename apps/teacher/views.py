from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import TeacherForm, RegistrationForm, CustomAuthenticationForm
from .models import UserTeacher


class RegisterView(CreateView):

    template_name: str = "register.html"
    form_class = RegistrationForm
    model = UserTeacher
    success_url = reverse_lazy("login")



class ProfileView(View):

    def get(self, request):
        return render(
            request,
            "profile.html"
        )


class SignIn(LoginView):
    template_name: str = "sign-in.html"

    def get_success_url(self) -> str:
        return reverse_lazy("profile")
    
