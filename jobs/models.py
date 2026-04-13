from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    collected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("title", "company", "location")

    def __str__(self) -> str:
        return self.title