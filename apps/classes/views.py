from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Classes
from .forms import ClassesForm



class CreateClassesView(CreateView):
    model = Classes
    fields = "__all__"
    template_name: str = "create_classes.html"
    success_url = reverse_lazy("teacher:profile")
    # form_class = ClassesForm

    # def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().post(request, *args, **kwargs)