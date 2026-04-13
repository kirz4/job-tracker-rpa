from django.shortcuts import render, redirect
from .models import Job
from django.conf import settings
from .scraper import scrape_jobs
from django.http import JsonResponse, HttpResponseForbidden



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
def refresh_jobs_api(request):
    secret = request.headers.get("X-SCRAPER-SECRET")

    if secret != settings.SCRAPER_SECRET:
        return HttpResponseForbidden("Unauthorized")

    jobs_data = scrape_jobs()

    saved = 0

    for item in jobs_data:
        obj, created = Job.objects.get_or_create(
            title=item["title"],
            company=item["company"],
            location=item["location"],
            defaults={"url": item["url"]},
        )

        if created:
            saved += 1

    return JsonResponse({
        "status": "ok",
        "new_jobs_saved": saved
    })