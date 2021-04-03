from django.shortcuts import render
from rest_framework import permissions, serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.
from django.conf import settings


class ContactView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer

    def post(self, request,*args,**kwargs):
        name= request.data.get("name", None)
        email= request.data.get("email", None)
        subject= request.data.get("subject", None)
        message= request.data.get("message", None)
        number= request.data.get("number", None)
        context = {
            "name":name,
        "email":email,
        "subject":subject,
        "message":message,
        "number":number
        }
        template = render_to_string('email.html', context)
        mail = EmailMessage(
                f"New Contact Email from {email}",
             template,
             settings.EMAIL_HOST_USER,
             [settings.EMAIL_HOST_USER],
            
            )    
        mail.fail_silently=False
        mail.send()

        contact =Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            number=number
        )
        contact.save()
        return Response(status=HTTP_200_OK)