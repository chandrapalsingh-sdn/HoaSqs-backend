from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Job
from .serializers import JobSerializer
from .tasks import send_job_to_queue

@api_view(["POST"])
def create_job(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "Text is required"}, status=400)

    job = Job.objects.create(text=text, status="pending")
    send_job_to_queue(job.id, job.text)
    return Response({"job_id": str(job.id)})

@api_view(["POST"])
def update_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    new_status = request.data.get("status")
    if new_status not in ["pending", "running", "done", "failed"]:
        return Response({"error": "Invalid status"}, status=400)
    job.status = new_status
    job.save()
    return Response({"job_id": str(job.id), "status": job.status})


@api_view(["GET"])
def job_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return Response({"job_id": str(job.id), "status": job.status})
