from django import forms
from .models import (company, company_log, orgid,
                     arcade_user_log, arcade_user, subscription_history,
                     subscription_history_log, interaction, interaction_log,
                     profile, profile_photo, label, xr_user, xr_user_log,
                     xr_subscription_history, xr_sub_history_log, generator,
                     id_generator)
STATUS_CHOICES = [
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Inactive'),
]
YN_CHOICES = [('YES', 'Yes'), ('NO', 'No'),]


class NewCompany(forms.ModelForm):
    '''Create a new company and add it to log record.'''
    class Meta:
        model = company
        fields = ['cname', 'poc_firstname', 'poc_lastname',
                  'poc_email', 'client_status', 'arcade_access_status',
                  'custom_deliverables', 'syndicated_reports',
                  'contract', 'xr_status']

        widgets = {
            'client_status':forms.Select(choices=STATUS_CHOICES),
            'arcade_access_status':forms.Select(choices=STATUS_CHOICES),
            'custom_deliverables':forms.Select(choices=YN_CHOICES),
            'syndicated_reports':forms.Select(choices=YN_CHOICES),
            'xr_status':forms.Select(choices=STATUS_CHOICES),

        }
    def writeord(self):
    #     data = self.cleaned_data
        log_record = orgid.objects.create(orgid_value=generator())
        return log_record


    def log(self):
        data = self.cleaned_data
        c_log = company_log(cname=data['cname'],
                            poc_firstname=data['poc_firstname'],
                            poc_lastname=data['poc_lastname'],
                            poc_email=data['poc_email'],
                            client_status=data['client_status'],
                            arcade_access_status=data['arcade_access_status'],
                            custom_deliverables=data['custom_deliverables'],
                            syndicated_reports=data['syndicated_reports'],
                            contract=data['contract'],
                            xr_status=data['xr_status'],
                            )
        return c_log

class DateInput(forms.DateInput):
    input_type = 'date'

class NewInteraction(forms.ModelForm):
    class Meta:
        model = interaction
        fields = ['dates_of_last_contact', 'notes',]
        widgets = {
            'dates_of_last_contact': DateInput()
        }

    def log(self):
        data = self.cleaned_data
        inter_log = interaction_log(
            dates_of_last_contact=data['dates_of_last_contact'], notes=data['notes'])
        return inter_log


class NewSubscription(forms.ModelForm):
    class Meta:
        model = subscription_history
        fields = ['subscription_start', 'subscription_end',]
        widgets = {
            'subscription_start': DateInput(),
            'subscription_end': DateInput(),
        }
    def log(self):
        data = self.cleaned_data
        sub_log = subscription_history_log(
            subscription_start=data['subscription_start'],
            subscription_end=data['subscription_end'])
        return sub_log

class NewAccount(forms.ModelForm):
    arcade_user_email = forms.EmailField(required=False)
    class Meta:
        model = arcade_user
        fields = ['arcade_user_id', 'arcade_user_firstname',
                  'arcade_user_lastname', 'arcade_user_email',
                  'aracde_user_status',]
        widgets = {
            'aracde_user_status': forms.Select(choices=STATUS_CHOICES)
        }

    def log(self):
        data = self.cleaned_data
        account_log = arcade_user_log(
            arcade_user_id=data['arcade_user_id'],
            arcade_user_firstname=data['arcade_user_firstname'],
            arcade_user_lastname=data['arcade_user_lastname'],
            arcade_user_email=data['arcade_user_email'],
            aracde_user_status=data['aracde_user_status'])
        return account_log

class NewXRAccount(forms.ModelForm):
    xr_user_email = forms.EmailField(required=False)
    class Meta:
        model = xr_user
        fields = ['xr_user_firstname',
                  'xr_user_lastname', 'xr_user_email',
                  'xr_user_status',]
        widgets = {
            'xr_user_status': forms.Select(choices=STATUS_CHOICES)
        }
    def log(self):
        data = self.cleaned_data
        user_log = xr_user_log(
            xr_user_firstname=data['xr_user_firstname'],
            xr_user_lastname=data['xr_user_lastname'],
            xr_user_email=data['xr_user_email'],
            xr_user_status=data['xr_user_status'])
        return user_log

class NewXRSubscription(forms.ModelForm):
    class Meta:
        model = xr_subscription_history
        fields = ['xr_subscription_start', 'xr_subscription_end', 'xr_tier']
        widgets = {
            'xr_subscription_start': DateInput(),
            'xr_subscription_end': DateInput(),
        }
    def log(self):
        data = self.cleaned_data
        sub_log = xr_sub_history_log(
            subscription_start=data['xr_subscription_start'],
            subscription_end=data['xr_subscription_end'],
            xr_tier=data['xr_tier'],
            )
        return sub_log


class EditCompany(forms.ModelForm):
    class Meta:
        model = company
        fields = ['cname', 'poc_firstname', 'poc_lastname',
                  'poc_email', 'client_status', 'arcade_access_status',
                'custom_deliverables', 'syndicated_reports',
                  'contract', 'company_label', 'xr_status',]
        widgets = {
            'client_status':forms.Select(choices=STATUS_CHOICES),
            'arcade_access_status':forms.Select(choices=STATUS_CHOICES),
            'custom_deliverables':forms.Select(choices=YN_CHOICES),
            'syndicated_reports':forms.Select(choices=YN_CHOICES),
            'xr_status':forms.Select(choices=STATUS_CHOICES),
        }

    def log(self):
        data = self.cleaned_data
        c_log = company_log(cname=data['cname'],
                            poc_firstname=data['poc_firstname'],
                            poc_lastname=data['poc_lastname'],
                            poc_email=data['poc_email'],
                            client_status=data['client_status'],
                            arcade_access_status=data['arcade_access_status'],
                            custom_deliverables=data['custom_deliverables'],
                            syndicated_reports=data['syndicated_reports'],
                            contract=data['contract'],
                            label=data['company_label'],
                            xr_status=data['xr_status'],)
        return c_log

class UploadPic(forms.ModelForm):
    class Meta:
        model = profile_photo
        fields = ['upload_photo', ]
        # widgets = {'upload_photo':forms.FileInput(
        #     attrs={'style':'display: none;', 'class':'form-control', 'required': False, }
        # )}

class EditProfile(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['position', 'phone', 'steam_id', 'twitter_id', 'epic_id', 'switch_id',
                  'blizzard_id', 'playstation_id', 'instagram_id', 'discord_id',
                  'description', 'twitch_id', 'riot_id']

        widgets = {
            'description': forms.Textarea(attrs={'rows':4})
        }

