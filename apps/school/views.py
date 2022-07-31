from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import School
from .forms import SchoolForm


class CreateSchoolView(CreateView):
    model = School
    fields = "__all__"
    template_name: str = "create_school.html"
    success_url = reverse_lazy("teacher:profile")
    # form_class = SchoolForm