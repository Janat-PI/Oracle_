from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse


from .forms import StudentForm, SendForm
from .models import Student


class CreateStudentView(CreateView):
    
    template_name: str = "create_student.html"
    form_class = StudentForm
    success_url = reverse_lazy("teacher:profile")



class ReadStudentView(ListView):
    model = Student
    template_name: str = "list-view.html"

    def get_queryset(self):
        return super().get_queryset().values(
            "first_name",
            "full_name",
            "sex",
            "address",
            "email"
        )


class DeleteStudentView(View):

    def get(self, request, pk: int):
        student = get_object_or_404(Student, pk=pk)
        name = student.first_name[::]
        student.delete()
        return render(
            request,
            "delete_student.html",
            locals()
        )



class UpdateStudentView(UpdateView):

    model = Student
    fields = "__all__"
    template_name: str = "student_update_form.html"

    def get_success_url(self) -> str:
        return reverse_lazy("teacher:profile")


class FindStudentView(View):


    def get(self, request):
        first_name = request.GET.get("first_name")
        queryset = Student.objects.filter(first_name__icontains=first_name)
        return render(
            request,
            "find_student.html",
            locals()
        )


class SendMessageView(View):

    
    def get(self, request, pk: int):
        
        student = get_object_or_404(Student, pk=pk)
        user = request.user 
    
        return render(
            request,
            "send_message.html",
            locals()
        )
    
    def post(self, request, pk: int = None):
        student = get_object_or_404(Student, pk=pk)
        data = request.POST
        form = SendForm(data=data, request=request, email=student.email)
        if form.is_valid():
            form.save()
            return redirect("teacher:profile")
        return HttpResponse("произошла проблема!!!")


        
        