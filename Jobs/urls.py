from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobscheduler/', include('JobScheduler.urls')),
    path('', lambda request: redirect('jobscheduler/job-form/')),  # Redirect to job-form by default
]
