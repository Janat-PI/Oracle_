from django.urls import path

from .views import CreateClassesView

app_name = "classes"

urlpatterns = [
    path("create/", CreateClassesView.as_view(), name="create_classes")
]