# your_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume_app.urls')),  # Include the URLs from your 'resume_app'
    # Add more paths for other apps as needed
]
