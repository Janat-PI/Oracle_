from django.urls import path

from .views import (
    CreateStudentView, ReadStudentView, 
    DeleteStudentView, UpdateStudentView,
    FindStudentView,
)

app_name = "student"

urlpatterns = [
    path("create/", CreateStudentView.as_view()),
    path("read/", ReadStudentView.as_view()),
    path("delete/<int:pk>/", DeleteStudentView.as_view(), name="delete"),
    path("update/<int:pk>/", UpdateStudentView.as_view(), name="update"),
    path("find/", FindStudentView.as_view(), name="find")
]