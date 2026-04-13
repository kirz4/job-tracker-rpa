from django.core.management.base import BaseCommand
from jobs.models import Job
from jobs.scraper import scrape_jobs


class Command(BaseCommand):
    help = "Executa o scraping de vagas e salva no banco"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Iniciando coleta de vagas..."))

        jobs_data = scrape_jobs()
        created_count = 0

        for item in jobs_data:
            _, created = Job.objects.get_or_create(
                url=item["url"],
                defaults={
                    "title": item["title"],
                    "company": item["company"],
                    "location": item["location"],
                },
            )

            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Coleta finalizada. {created_count} novas vagas salvas."))