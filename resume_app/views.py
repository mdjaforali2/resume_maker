# resume_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import UserInfo, ResumeFormat
from .forms import UserInfoForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserInfoForm, Education, Experience, Reference, TechnicalSkill, SoftSkill, LanguageKnown, Certification, EducationForm, ExperienceForm, SoftSkillForm, TechnicalSkillForm, LanguageKnownForm, CertificationForm, ReferenceForm 
from django.forms import inlineformset_factory
from django.contrib import messages
from django.template.loader import render_to_string





def home(request):
    return render(request, 'resume_app/home.html')


@login_required(login_url='login')
def input_info(request):
    user_info, created = UserInfo.objects.get_or_create(email=request.user.email)

    # Use the correct formset factory name
    EducationFormSet = inlineformset_factory(UserInfo, Education, form=EducationForm, extra=1, can_delete=True)
    ExperienceFormSet = inlineformset_factory(UserInfo, Experience, form=ExperienceForm, extra=1, can_delete=True)
    ReferenceFormSet = inlineformset_factory(UserInfo, Reference, form=ReferenceForm, extra=1, can_delete=True)
    TechnicalSkillFormSet = inlineformset_factory(UserInfo, TechnicalSkill, form=TechnicalSkillForm, extra=1, can_delete=True)
    SoftSkillFormSet = inlineformset_factory(UserInfo, SoftSkill, form=SoftSkillForm, extra=1, can_delete=True)
    LanguageKnownFormSet = inlineformset_factory(UserInfo, LanguageKnown, form=LanguageKnownForm, extra=1, can_delete=True)
    CertificationFormSet = inlineformset_factory(UserInfo, Certification, form=CertificationForm, extra=1, can_delete=True)

    formset_instances = {
        'education_formset': EducationFormSet,
        'experience_formset': ExperienceFormSet,
        'reference_formset': ReferenceFormSet,
        'technical_skill_formset': TechnicalSkillFormSet,
        'soft_skill_formset': SoftSkillFormSet,
        'language_formset': LanguageKnownFormSet,
        'certification_formset': CertificationFormSet,
    }

    formsets = {}

    for formset_name, formset_instance in formset_instances.items():
        formsets[formset_name] = formset_instance(instance=user_info, prefix=formset_name)

    if request.method == 'POST':
        user_info_form = UserInfoForm(request.POST, instance=user_info)

        # Process the main user_info_form first
        if user_info_form.is_valid():
            user_info_form.save()
            messages.success(request, "User Info Form saved successfully")
        else:
            messages.error(request, f"User Info Form errors: {user_info_form.errors}")

        for formset_name, formset_instance in formset_instances.items():
            formset = formset_instance(request.POST, instance=user_info, prefix=formset_name)
            if formset.is_valid():
                # Associate the formset with the user_info instance
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user_info = user_info
                    instance.save()
                messages.success(request, f"{formset_name.capitalize()} Formset saved successfully")
            else:
                messages.error(request, f"{formset_name.capitalize()} Formset errors: {formset.errors}")

        # Redirect to the 'format_selection' page
        if request.POST.get('action') == 'save_and_continue':
                return redirect('format_selection')
        elif request.POST.get('action') == 'add':
                return redirect('input_info')


    else:
        user_info_form = UserInfoForm(instance=user_info)

    return render(request, 'resume_app/input_info.html', {
        'user_info_form': user_info_form,
        **formsets,  # Use the formsets in the context
    })


def format_selection(request):
    user_info_id = request.user.id
    user_info = UserInfo.objects.get(id=user_info_id)
    resume_formats = ResumeFormat.objects.all()

    return render(request, 'resume_app/format_selection.html', {'user_info': user_info, 'resume_formats': resume_formats})



def generate_pdf(request, user_info_id, format_id):
    user_info = get_object_or_404(UserInfo, id=user_info_id)
    resume_format = get_object_or_404(ResumeFormat, id=format_id)

    template_path = resume_format.template_path
    context = {'user_info': user_info}

    # Render HTML content
    html_content = render_to_string(template_path, context)

    # Create an HttpResponse with the HTML content
    response = HttpResponse(content_type='text/html')
    response['Content-Disposition'] = f'filename={user_info.first_name}_{user_info.last_name}_resume.html'
    response.write(html_content)

    return response


def download_pdf(request, user_info_id, format_id):
    user_info = get_object_or_404(UserInfo, id=user_info_id)
    resume_format = get_object_or_404(ResumeFormat, id=format_id)

    template_path = resume_format.template_path
    context = {'user_info': user_info}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={user_info.first_name}_{user_info.last_name}_resume.pdf'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error creating PDF')

    return response


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def preview_format(request, user_info_id, format_id):
    user_info = get_object_or_404(UserInfo, id=user_info_id)
    resume_format = get_object_or_404(ResumeFormat, id=format_id)

    template_path = resume_format.template_path
    context = {'user_info': user_info}

    return render(request, template_path, context)

