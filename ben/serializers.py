from django.db.models import fields
from rest_framework import serializers
from .models import Contact, Reviews

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields=(
            "name",
"email",
"subject",
"message",
        )


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields=(
            "name",
            "email",
            "feel",
            "number",
            "rating",
            "recommend",
            "suggest",
            "social",
            "comment",
            "photo",
        
        )