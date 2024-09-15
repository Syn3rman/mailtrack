from django.urls import path
from .views import GetTrackingPixelView, TrackEmailOpenView, UserEmailsView

urlpatterns = [
    path('get-tracking-pixel/', GetTrackingPixelView.as_view()),
    path('track-email-open/<str:tracking_pixel_id>/', TrackEmailOpenView.as_view()),
    path('user-emails/', UserEmailsView.as_view()),
]