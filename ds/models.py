from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from datetime import datetime, timedelta
from pytz import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rekt.storage_backends import photo_storage

class profile_photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    upload_photo = models.ImageField(storage=photo_storage())
    updated_by = models.ForeignKey(
        User, related_name="UpdatedPhotos", on_delete=models.CASCADE, blank=True)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    position = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    steam_id = models.CharField(max_length=255, blank=True)
    twitter_id = models.CharField(max_length=255, blank=True)
    twitch_id = models.CharField(max_length=255, blank=True)
    epic_id = models.CharField(max_length=255, blank=True)
    switch_id = models.CharField(max_length=255, blank=True)
    blizzard_id = models.CharField(max_length=255, blank=True)
    playstation_id = models.CharField(max_length=255, blank=True)
    instagram_id = models.CharField(max_length=255, blank=True)
    discord_id = models.CharField(max_length=255, blank=True)
    riot_id = models.CharField(max_length=255, blank=True)
    photo = models.OneToOneField(
        profile_photo, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def est():
    local_time = datetime.now(timezone('US/Eastern'))
    return local_time.replace(tzinfo=None)

class label(models.Model):
    label_id = models.IntegerField(blank=True, primary_key=True)
    label_name = models.CharField(max_length=30)
    def __str__(self):
        return self.label_name

class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    orgid = models.CharField(max_length=50, unique=True)
    cname = models.CharField(max_length=50)
    poc_firstname = models.CharField(max_length=30, blank=True)
    poc_lastname = models.CharField(max_length=30, blank=True)
    poc_email = models.EmailField(max_length=250, blank=True)
    client_status = models.CharField(max_length=30)
    arcade_access_status = models.CharField(max_length=30)
    xr_status = models.CharField(max_length=30, default="INACTIVE")
    arcade_id = models.IntegerField(blank=True, null=True)
    custom_deliverables = models.CharField(max_length=10)
    syndicated_reports = models.CharField(max_length=10)
    company_label = models.ForeignKey(
        label, related_name="clients_labeled", on_delete=models.CASCADE,
        blank=True, null=True
    )
    contract = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.cname
    class Meta:
        verbose_name_plural = "companies"

class arcade_user(models.Model):
    id = models.AutoField(primary_key=True)
    arcade_user_id = models.CharField(max_length=30)
    arcade_user_firstname = models.CharField(max_length=30)
    arcade_user_lastname = models.CharField(max_length=30)
    arcade_user_email = models.EmailField(max_length=250)
    aracde_user_status = models.CharField(max_length=15)
    company_id = models.ForeignKey(
        company, related_name="arcade_user", on_delete=models.CASCADE)
    def __str__(self):
        return self.arcade_user_email

class subscription_history(models.Model):
    sub_id = models.AutoField(primary_key=True)
    subscription_start = models.DateField()
    subscription_end = models.DateField()
    company_id = models.ForeignKey(
        company, related_name="subscription_history", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.sub_id)
    class Meta:
        verbose_name_plural = "subscription_histories"

class xr_user(models.Model):
    id = models.AutoField(primary_key=True)
    xr_user_firstname = models.CharField(max_length=30)
    xr_user_lastname = models.CharField(max_length=30)
    xr_user_email = models.CharField(max_length=250)
    xr_user_status = models.CharField(max_length=15, default="INACTIVE")
    company_id = models.ForeignKey(
        company, related_name="xr_user", on_delete=models.CASCADE
    )

class xr_subscription_history(models.Model):
    xr_sub_id = models.AutoField(primary_key=True)
    xr_subscription_start = models.DateField()
    xr_subscription_end = models.DateField()
    xr_tier = models.CharField(max_length=20)
    company_id = models.ForeignKey(
        company, related_name="xr_sub_history", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.xr_sub_id)
    class Meta:
        verbose_name_plural = "xr_subscription_histories"

class interaction(models.Model):
    interaction_id = models.AutoField(primary_key=True)
    dates_of_last_contact = models.DateField()
    notes = models.TextField(max_length=4000)
    company_id = models.ForeignKey(
        company, related_name="interaction", on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User, related_name="notes", on_delete=models.CASCADE)

    def __str__(self):
        truncated_notes = Truncator(self.notes)
        return truncated_notes.chars(30)

########################################################################
#########################Data Schedule Log##############################
########################################################################

class orgid(models.Model):
    orgid = models.AutoField(primary_key=True)
    orgid_value = models.CharField(
        max_length=50, unique=True, default='DEFAULT VALUE')
    def __str__(self):
        return self.orgid_value


class company_log(models.Model):
    company_log_id = models.AutoField(primary_key=True)
    orgid = models.ForeignKey(
        orgid, related_name="company_log", on_delete=models.CASCADE, null=True)
    cname = models.CharField(max_length=100)
    poc_firstname = models.CharField(max_length=30, blank=True)
    poc_lastname = models.CharField(max_length=30, blank=True)
    poc_email = models.EmailField(max_length=250, blank=True)
    client_status = models.CharField(max_length=30)
    arcade_access_status = models.CharField(max_length=30)
    xr_status = models.CharField(max_length=30, default="INACTIVE")
    arcade_id = models.IntegerField(blank=True, null=True)
    custom_deliverables = models.CharField(max_length=10)
    syndicated_reports = models.CharField(max_length=10)
    ftp_access = models.CharField(max_length=10)
    updated_by = models.ForeignKey(
        User, null=True, related_name="company_editor", on_delete=models.CASCADE)
    time = models.DateTimeField(default=est)
    log_notes = models.CharField(max_length=100)
    contract = models.CharField(max_length=250, blank=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.cname


class arcade_user_log(models.Model):
    arcade_user_log_id = models.AutoField(primary_key=True)
    arcade_user_id = models.CharField(max_length=30)
    arcade_user_firstname = models.CharField(max_length=30)
    arcade_user_lastname = models.CharField(max_length=30)
    arcade_user_email = models.EmailField(max_length=250)
    aracde_user_status = models.CharField(max_length=15)
    orgid = models.ForeignKey(
        orgid, related_name="aruser_log", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name="aruser_editor", on_delete=models.CASCADE)
    time = models.DateTimeField(default=est)
    log_notes = models.CharField(max_length=100)
    def __str__(self):
        return self.arcade_user_id

class xr_user_log(models.Model):
    xr_user_log_id = models.AutoField(primary_key=True)
    xr_user_firstname = models.CharField(max_length=30)
    xr_user_lastname = models.CharField(max_length=30)
    xr_user_email = models.EmailField(max_length=250)
    xr_user_status = models.CharField(max_length=15)
    orgid = models.ForeignKey(
        orgid, related_name="xr_user_log", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name="xr_user_editor", on_delete=models.CASCADE)
    time = models.DateTimeField(default=est)
    log_notes = models.CharField(max_length=100)
    def __str__(self):
        return self.xr_user_id



class subscription_history_log(models.Model):
    sub_id_log = models.AutoField(primary_key=True)
    sub_id = models.IntegerField()
    subscription_start = models.DateField()
    subscription_end = models.DateField()
    orgid = models.ForeignKey(
        orgid, related_name="sub_his_log", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name="sub_his_editor", on_delete=models.CASCADE)
    time = models.DateTimeField(default=est)
    log_notes = models.CharField(max_length=100)

class xr_sub_history_log(models.Model):
    xr_sub_id_log = models.AutoField(primary_key=True)
    xr_sub_id = models.IntegerField()
    subscription_start = models.DateField()
    subscription_end = models.DateField()
    xr_tier = models.CharField(max_length=20)
    orgid = models.ForeignKey(
        orgid, related_name="xr_sub_his_log", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name="xr_sub_his_editor", on_delete=models.CASCADE)
    time = models.DateTimeField(default=est)
    log_notes = models.CharField(max_length=100)

class interaction_log(models.Model):
    interaction_log_id = models.AutoField(primary_key=True)
    interaction_id = models.IntegerField()
    dates_of_last_contact = models.DateField()
    notes = models.TextField(max_length=4000)
    orgid = models.ForeignKey(
        orgid, related_name="inter_log", on_delete=models.CASCADE)
    userid = models.ForeignKey(
        User, related_name="inter_log_creator", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name="inter_editor", on_delete=models.CASCADE)
    time = models.DateTimeField(default=est)
    log_notes = models.CharField(max_length=100)

    def __str__(self):
        truncated_notes = Truncator(self.notes)
        return truncated_notes.chars(30)


# class ActiveArcadeSubscriptions(models.Model):
#     subscription_id = models.CharField(
#         max_length=12, blank=True, primary_key=True)
#     company_name = models.CharField(max_length=255, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     ftp = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'active_arcade_subscriptions'

class ArcadeSubscriptionsRekt(models.Model):
    subscription_id = models.IntegerField(blank=True, primary_key=True)
    subscription = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arcade_subscriptions_rekt'

class PageSummary(models.Model):
    username = models.CharField(max_length=255, blank=True, primary_key=True)
    page = models.CharField(max_length=50, blank=True, null=True)
    time_spent = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'page_summary'

class ActiveArcadeSubscriptions(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ftp = models.IntegerField(blank=True, null=True)
    access_level = models.CharField(max_length=255, blank=True, null=True)
    access_max_month_year = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_arcade_subscriptions'

class GatekeeperLogAccount(models.Model):
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=255)
    subscription_id = models.IntegerField()
    company_name = models.CharField(max_length=255)
    client_status = models.IntegerField()
    product_access = models.CharField(max_length=255)
    full_access = models.IntegerField()
    ftp_access = models.IntegerField()
    data_access = models.DateTimeField(blank=True, null=True)
    action_taken = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'gatekeeper_log_account'


class GatekeeperLogSubscription(models.Model):
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=255)
    subscription_id = models.IntegerField()
    permission_id = models.IntegerField()
    action_taken = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'gatekeeper_log_subscription'


class GatekeeperLogUser(models.Model):
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=255)
    subscription_id = models.IntegerField()
    user_full_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    account_status = models.IntegerField()
    action_taken = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'gatekeeper_log_user'

class PermissionMaster(models.Model):
    permission_id = models.AutoField(primary_key=True)
    subscription_id = models.IntegerField(blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    main_criterion = models.CharField(max_length=255, blank=True, null=True)
    mc_value = models.CharField(max_length=255, blank=True, null=True)
    second_criterion = models.CharField(max_length=255, blank=True, null=True)
    sc_value = models.CharField(max_length=255, blank=True, null=True)
    third_criterion = models.CharField(max_length=255, blank=True, null=True)
    tc_value = models.CharField(max_length=255, blank=True, null=True)
    fourth_criterion = models.CharField(max_length=255, blank=True, null=True)
    fc_value = models.CharField(max_length=255, blank=True, null=True)
    permission_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission_master'

class UsersEmailMapping(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    org_id = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=8, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    access_level = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_email_mapping'
        
