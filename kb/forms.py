from django import forms
from .models import category, faq, answer, tag

class FAQForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = ['subject', ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = answer
        fields = ['answer',]


class TagForm(forms.ModelForm):
    class Meta:
        model = tag
        fields = ['tag_name',]

class QuetionTagForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = ['tag_faq',]
