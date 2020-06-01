from django.db import models

# Create your models here.
class UploadProgressCurrent(models.Model):
    current_process = models.CharField(max_length=255, blank=True, primary_key=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_elapsed = models.CharField(max_length=20, blank=True, null=True)
    current_upload_type = models.CharField(max_length=20, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'upload_progress_current'


class UploadProgressCount(models.Model):
    maxdate = models.DateField(blank=True, null=True)
    upload_type = models.CharField(max_length=20, blank=True, null=True)
    upload_id = models.CharField(max_length=12, blank=True, null=True)
    count_num = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'upload_progress_count'



class SandboxLogLive(models.Model):
    time_stamp = models.DateTimeField(primary_key=True)
    log_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sandbox_log_live'

class SandboxLogEarlyaccess(models.Model):
    time_stamp = models.DateTimeField(primary_key=True)
    log_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sandbox_log_earlyaccess'



class UploadProgressHistorical(models.Model):
    upload_id = models.CharField(max_length=12, blank=True, null=True)
    current_process = models.CharField(max_length=255, blank=True, null=True)
    time_start = models.DateTimeField(primary_key=True)
    time_elapsed = models.CharField(max_length=20, blank=True, null=True)
    upload_type = models.CharField(max_length=20, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_progress_historical'

class WebsiteStatus(models.Model):
    website = models.CharField(max_length=255, blank=True, null=True)
    percent_loss = models.FloatField(blank=True, null=True)
    check_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_status'

class WebsiteInfo(models.Model):
    website_address = models.CharField(max_length=255, blank=True, null=True)
    website_display = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_info'

class WebsitePingResult(models.Model):
    website = models.ForeignKey('WebsiteInfo', models.CASCADE, db_column='website')
    percent_loss = models.FloatField(blank=True, null=True)
    check_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_ping_result'


# class RoadmapUrls(models.Model):
#     roadmap_title = models.CharField(max_length=255, blank=True, null=True)
#     roadmap_url = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'roadmap_urls'
