# Generated by Django 4.2.7 on 2023-12-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_alter_languageknown_language_alter_softskill_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='gpa_obtained',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='gpa_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
