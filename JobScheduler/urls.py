from django.urls import path
from .views import job_form, submit_jobs

urlpatterns = [
    path('', job_form, name='job_form'),   # Handle the root URL
    path('job-form/', job_form, name='job_form'),   # Example URL for job form
    path('submit/', submit_jobs, name='submit_jobs'),   # Example URL for job submission
]
