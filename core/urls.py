from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_jobs(request):
    return redirect("/jobs/")


urlpatterns = [
    path("", redirect_to_jobs),
    path("admin/", admin.site.urls),
    path("jobs/", include("jobs.urls")),
]