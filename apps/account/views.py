from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse

from .forms import RegistrationForm


User = get_user_model()

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name: str = "register.html"
    success_url = reverse_lazy("profile")


class ProfileView(View):

    def get(self, request):
        return render(
            request,
            "profile.html"
        )