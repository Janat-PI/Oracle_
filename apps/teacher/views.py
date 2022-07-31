from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import  RegistrationForm
from .models import UserTeacher

from ..student.models import Student


class RegisterView(CreateView):

    template_name: str = "register.html"
    form_class = RegistrationForm
    model = UserTeacher
    success_url = reverse_lazy("teacher:login")


class ProfileView(View):

    def get(self, request):
        # student_list = Student.objects.values(
        #     "first_name",
        #     "full_name",
        #     "sex",
        #     "address",
        #     "email",
        #     "pk",
        #     "image",
        #     "classes__title"
        # )

        student_list = Student.objects.all()

        return render(
            request,
            "profile.html",
            locals()
        )


class SignIn(LoginView):
    template_name: str = "sign-in.html"

    def get_success_url(self) -> str:
        return reverse_lazy("teacher:profile")
    

