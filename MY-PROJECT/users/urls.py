from django.urls import path
from .views import UserProfileView
from .views import UserRegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import LoginView



urlpatterns = [
    path('', UserProfileView.as_view(), name='user-default'),  # Add this for the base route
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For obtaining tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('login/', LoginView.as_view(), name='user-login'),
 
]
