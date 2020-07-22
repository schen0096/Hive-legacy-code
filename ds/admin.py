from django.contrib import admin
from .models import (company, arcade_user, subscription_history,
                     interaction, orgid, arcade_user_log, company_log,
                     subscription_history_log, interaction_log, label,
                     profile, profile_photo)
# Register your models here.
admin.site.register(company)
admin.site.register(arcade_user)
admin.site.register(subscription_history)
admin.site.register(interaction)
admin.site.register(orgid)

admin.site.register(arcade_user_log)
admin.site.register(company_log)
admin.site.register(subscription_history_log)
admin.site.register(interaction_log)
admin.site.register(label)
admin.site.register(profile)
admin.site.register(profile_photo)
