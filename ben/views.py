from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ContactSerializer, ReviewsSerializer
from .models import Contact, Reviews
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

class ReviewCreateView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request, *args, **kwargs):
        name = request.data.get("name", None)
        email = request.data.get("email", None)
        feel = request.data.get("feel", None)
        number = request.data.get("number", None)
        rating = request.data.get("rating", None)
        recommend = request.data.get("recommend", None)
        suggest = request.data.get("suggest", None)
        social = request.data.get("social", None)
        comment = request.data.get("comment", None)
        photo = request.FILES.get("photo", None)

        reviews = Reviews(
            name=name,
            email=email,
            feel=feel,
            number=number,
            rating=rating,
            recommend=recommend,
            suggest=suggest,
            social=social,
            comment=comment,
            photo=photo
        )
        reviews.save()
        return Response(status=HTTP_200_OK)

class ReviewsListView(ListAPIView):
    queryset = Reviews.objects.all().order_by('-date')
    serializer_class = ReviewsSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Reviews.objects.all().order_by('-date')

class ReviewsListHomeView(ListAPIView):
    queryset = Reviews.objects.all().order_by('-date')[:3]
    serializer_class = ReviewsSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Reviews.objects.all().order_by('-date')[:3]

        