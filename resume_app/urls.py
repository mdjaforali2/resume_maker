# resume_app/urls.py
from django.urls import path
from .views import home, input_info, format_selection, generate_pdf, download_pdf, preview_format
from .views import login_view, signup_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),  # Maps the root URL to the home view
    path('input/', input_info, name='input_info'),
    path('format/', format_selection, name='format_selection'),
    path('preview/<int:user_info_id>/<int:format_id>/', preview_format, name='preview_format'),

    path('generate_pdf/<int:user_info_id>/<int:format_id>/', generate_pdf, name='generate_pdf'),
    path('download_pdf/<int:user_info_id>/<int:format_id>/', download_pdf, name='download_pdf'),
        # Login view
    path('login/', login_view, name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Signup view
    path('signup/', signup_view, name='signup'),

    # Add more paths for other views as needed
]
