from django.urls import path
from .views import JobAppView, JobAppThanks

app_name = 'jobs'
urlpatterns = [
    path('job-app/', JobAppView.as_view(), name='app'),
    path('job-app/thanks/', JobAppThanks.as_view(), name='thanks'),
]
