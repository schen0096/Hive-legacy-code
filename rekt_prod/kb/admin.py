from django.contrib import admin
from .models import category, faq, answer, tag, faq_log

# Register your models here.
admin.site.register(category)
admin.site.register(faq)
admin.site.register(answer)
admin.site.register(tag)
admin.site.register(faq_log)
