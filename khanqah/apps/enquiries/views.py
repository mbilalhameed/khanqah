import send_email as send_email
from django.core.mail import send_mail

from rest_framework import permissions
from rest_framework.decorators import APIView, permission_classes
from rest_framework.response import Response

from khanqah.settings.development import DEFAULT_FROM_EMAIL
from .models import Enquiry


@APIView(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = data[DEFAULT_FROM_EMAIL]

        send_email(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted."})

    except:
        return Response({"fail": "Your Enquiry was not submitted"})
