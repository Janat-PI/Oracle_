from django.urls import path

from .views import CreateView


urlpatterns = [
    path("create/", CreateView.as_view()),
    # path("profile/", ProfileView.as_view(), name="profile")
]