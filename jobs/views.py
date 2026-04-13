from django.shortcuts import render, redirect
from .models import Job
from .scraper import scrape_jobs
from django.http import JsonResponse



def job_list(request):
    query = request.GET.get("q", "")
    jobs = Job.objects.all().order_by("-collected_at", "title")

    if query:
        jobs = jobs.filter(title__icontains=query)

    context = {
        "jobs": jobs,
        "query": query,
        "total_jobs": jobs.count(),
    }
    return render(request, "jobs/job_list.html", context)


def refresh_jobs(request):
    if request.method == "POST":
        jobs_data = scrape_jobs()

        for item in jobs_data:
            Job.objects.get_or_create(
                title=item["title"],
                company=item["company"],
                location=item["location"],
                defaults={
                    "url": item["url"],
                },
            )

    return redirect("/jobs/")
def jobs_api(request):
    jobs = Job.objects.all().order_by("-collected_at")[:50]

    data = [
        {
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "url": job.url,
            "collected_at": job.collected_at,
        }
        for job in jobs
    ]

    return JsonResponse({"jobs": data})