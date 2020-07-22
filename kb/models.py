from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from pytz import timezone
# Create your models here.
def est():
    local_time = datetime.now(timezone('US/Eastern'))
    return local_time.replace(tzinfo=None)

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    def __str__(self):
        return self.tag_name

class faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=est)
    starter = models.ForeignKey(User, related_name='faq',
                                on_delete=models.CASCADE)
    category_id = models.ForeignKey(category,
                                    related_name='question',
                                    on_delete=models.CASCADE, null=True)
    tag_faq = models.ManyToManyField(tag)
    pin_value = models.BooleanField(default=False)
    def __str__(self):
        return self.subject

class answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(default=est)
    faq = models.ForeignKey(faq, related_name='answer',
                            on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='answer',
                                   on_delete=models.CASCADE)
    def __str__(self):
        return self.answer


class faq_log_id(models.Model):
    faq_log_id = models.AutoField(primary_key=True)
    faq_id_value = models.IntegerField(blank=True, null=True)

class faq_log(models.Model):
    faq_logging_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=est)
    answer = RichTextField(blank=True, null=True)
    editor = models.ForeignKey(User,
                               related_name='editor',
                               on_delete=models.CASCADE)
    category_id = models.ForeignKey(category,
                                    related_name='category_log',
                                    on_delete=models.CASCADE, null=True)
    faq_id = models.ForeignKey(faq_log_id,
                               related_name='faq_log',
                               on_delete=models.CASCADE)
    def __str__(self):
        return self.subject
