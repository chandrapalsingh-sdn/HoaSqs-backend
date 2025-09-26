from django.urls import path, include

urlpatterns = [
    path("api/jobs/", include("jobs.urls")),
]
