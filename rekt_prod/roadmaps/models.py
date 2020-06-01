from django.db import models
from datetime import datetime
from pytz import timezone

def est():
    local_time=datetime.now(timezone('US/Eastern'))
    return local_time.replace(tzinfo=None)


class arcade_weekly_roadmap(models.Model):
    late_updated=models.DateTimeField(default=est)
    roadmap=models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.late_updated)


class roadmap_urls(models.Model):
    roadmap_title = models.CharField(max_length=255, blank=True, null=True)
    roadmap_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roadmap_urls'
        verbose_name_plural = "roadmap_urls"

    def __str__(self):
        return str(self.roadmap_title)