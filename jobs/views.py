from django.shortcuts import render
from .models import Job


def job_list(request):
    query = request.GET.get("q", "")
    jobs = Job.objects.all().order_by("-collected_at")

    if query:
        jobs = jobs.filter(title__icontains=query)

    context = {
        "jobs": jobs,
        "query": query,
    }
    return render(request, "jobs/job_list.html", context)