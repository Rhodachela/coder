from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path('', UserProfileView.as_view(), name='user-default'),  # Add this for the base route
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
