from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField(unique=True)
    collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title