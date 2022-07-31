from django.urls import path

from .views import CreateSchoolView


app_name = "school"

urlpatterns = [
    path("create/", CreateSchoolView.as_view(), name="create_school")
]