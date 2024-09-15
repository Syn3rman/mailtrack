from rest_framework import serializers
from .models import Email, EmailOpen, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'subject', 'body', 'sender', 'recipient', 'tracking_pixel_id']

class EmailOpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOpen
        fields = ['id', 'email', 'opened_at']

class ReadOnlyEmailSerializer(serializers.ModelSerializer):
    opens = EmailOpenSerializer(many=True, read_only=True)

    class Meta:
        model = Email
        fields = ['id', 'subject', 'body', 'sender', 'recipient', 'tracking_pixel_id', 'opens']

class GetTrackingPixelSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField()
    recipient = serializers.EmailField()