# admin.py

from django.contrib import admin
from .models import (
    Certification, Reference,
    TechnicalSkill, SoftSkill, LanguageKnown, UserInfo, Education, Experience, ResumeFormat
)
from .forms import (
    CertificationForm, ReferenceForm, LanguageKnownForm, TechnicalSkillForm, SoftSkillForm,
    EducationForm, ExperienceForm, UserInfoForm
)

class EducationInline(admin.TabularInline):
    model = Education
    form = EducationForm
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    form = ExperienceForm
    extra = 1

class TechnicalSkillInline(admin.TabularInline):
    model = TechnicalSkill
    form = TechnicalSkillForm
    extra = 1


class SoftSkillInline(admin.TabularInline):
    model = SoftSkill
    form = SoftSkillForm
    extra = 1


class ReferenceInline(admin.TabularInline):
    model = Reference
    form = ReferenceForm
    extra = 1


class CertificationInline(admin.TabularInline):
    model = Certification
    form = CertificationForm
    extra = 1


class LanguageKnownInline(admin.TabularInline):
    model = LanguageKnown
    form = LanguageKnownForm
    extra = 1




class UserInfoAdmin(admin.ModelAdmin):
    form = UserInfoForm
    inlines = [
        EducationInline, ExperienceInline, TechnicalSkillInline, SoftSkillInline,  CertificationInline, LanguageKnownInline, ReferenceInline

    ]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(ResumeFormat)  # Include if needed
admin.site.register(TechnicalSkill)
admin.site.register(SoftSkill)
admin.site.register(Reference)
admin.site.register(Certification)
admin.site.register(LanguageKnown)
admin.site.register(Education)
admin.site.register(Experience)
# ... Register other models
