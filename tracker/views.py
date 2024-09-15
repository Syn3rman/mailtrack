from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Email, EmailOpen
from .serializers import ReadOnlyEmailSerializer, GetTrackingPixelSerializer
import uuid

class GetTrackingPixelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GetTrackingPixelSerializer(data=request.data)
        if serializer.is_valid():
            email = Email.objects.create(
                subject=serializer.validated_data['subject'],
                body=serializer.validated_data['body'],
                sender=request.user,
                recipient=serializer.validated_data['recipient'],
                tracking_pixel_id=uuid.uuid4()
            )

            return Response({'tracking_pixel_id': email.tracking_pixel_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TrackEmailOpenView(APIView):
    def get(self, request, tracking_pixel_id):
        try:
            email = Email.objects.get(tracking_pixel_id=tracking_pixel_id)
            ip_address = request.META.get('REMOTE_ADDR')
            EmailOpen.objects.create(email=email, ip_address=ip_address)
            return Response(status=status.HTTP_200_OK)
        except Email.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserEmailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        emails = Email.objects.filter(sender=request.user)
        serializer = ReadOnlyEmailSerializer(emails, many=True)
        return Response(serializer.data)
    