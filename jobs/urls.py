from django.urls import path
from .views import job_list, refresh_jobs
from .views import jobs_api
from .views import refresh_jobs_api

urlpatterns = [
    path("", job_list, name="job_list"),
    path("refresh/", refresh_jobs, name="refresh_jobs"),
    path("api/jobs/", jobs_api, name="jobs_api"),
    path("api/refresh/", refresh_jobs_api, name="refresh_jobs_api"),
]