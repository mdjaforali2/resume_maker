# forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import (
    Certification, Reference,
    TechnicalSkill, SoftSkill, LanguageKnown, UserInfo, Education, Experience
)

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'email', 'phone_number']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'url']

class LanguageKnownForm(forms.ModelForm):
    class Meta:
        model = LanguageKnown
        fields = ['language']

class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['name']

class SoftSkillForm(forms.ModelForm):
    class Meta:
        model = SoftSkill
        fields = ['name']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'graduation_year', 'gpa_total', 'gpa_obtained']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'country','city', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'post_code',
            'linkedin_profile', 'portfolio_website', 'github_profile', 'professional_summary','job_title'
        ]



