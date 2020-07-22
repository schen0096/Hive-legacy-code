from django import forms
from .models import arcade_weekly_roadmap,roadmap_urls


class RoadmapForm(forms.ModelForm):
    class Meta:
        model=arcade_weekly_roadmap
        fields=['roadmap']


class RoadmapUrlMap(forms.ModelForm):
    class Meta:
        model=roadmap_urls
        fields=['roadmap_url','roadmap_title']