# models.py

from django.db import models


class Reference(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Certification(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class LanguageKnown(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='languages_known')
    language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.language

class TechnicalSkill(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='technical_skills')
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class SoftSkill(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='soft_skills')
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    gpa_total = models.FloatField(blank=True, null=True)
    gpa_obtained = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution} ({self.graduation_year}) - GPA: {self.gpa_obtained}/{self.gpa_total}"

class Experience(models.Model):
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.company} ({self.city}, {self.country}) ({self.start_date} - {self.end_date})"


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    linkedin_profile = models.URLField(blank=True, null=True)
    portfolio_website = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    job_title = models.CharField(max_length=50)
    professional_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ResumeFormat(models.Model):
    name = models.CharField(max_length=50)
    template_path = models.CharField(max_length=100)  # path to the HTML template for this format

    def __str__(self):
        return self.name