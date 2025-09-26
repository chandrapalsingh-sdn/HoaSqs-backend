from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_job, name="create-job"),
    path("<uuid:job_id>/status/", views.job_status, name="job-status"),
]
