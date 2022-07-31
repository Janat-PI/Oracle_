from django.contrib import admin
from django.urls import path, include, reverse
from django.http import HttpResponseRedirect

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("teacher/", include("apps.teacher.urls", namespace="teacher")),
    path("school/", include("apps.school.urls", namespace="school")),
    path("student/", include("apps.student.urls", namespace="student")),
    path("classes/", include("apps.classes.urls", namespace="classes")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)