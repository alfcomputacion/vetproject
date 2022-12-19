import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from common.utils.email import send_mail
from .forms import JobApplicationForm
# Create your views here.


class JobAppView(FormView):
    template_name = 'jobs/job_message.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = ['alfcomputacion@gmail.com', 'info@centralstorage.com']
        subject = 'Aplication for Joke Writer'
        content = f'''<p>Hey HR Manager!</p>
                    <p>Job Application received:</p>
                    <ol>'''
        for key, value in data.items():
            label = key.replace('-', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        content += '</ol>'
        send_mail(to, subject, content)
        return super().form_valid(form)


class JobAppThanks(TemplateView):
    template_name = 'jobs/thanks.html'
