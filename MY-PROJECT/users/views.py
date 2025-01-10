from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

class LoginView(APIView):
    """
    Handles user login and token generation.
    """
    permission_classes = [AllowAny]  # Allow anyone to access the login endpoint

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        if not username or not password:
            return Response({
                "message": "Both username and password are required."
            }, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)  # Update the last login field

            return Response({
                "token": str(refresh.access_token),
                "refresh": str(refresh),
                "username": user.username,
                "email": user.email,
                "message": "Login successful"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            if user.is_authenticated:
                data = {
                    "username": user.username,
                    "email": user.email,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserRegistrationView(APIView):
    """
    Handles user registration.
    """
    permission_classes = [AllowAny]  # Allow access to anyone

    def post(self, request):
        data = request.data
        data['password'] = make_password(data.get('password'))  # Hash the password
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "message": "User registered successfully!"
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .serializers import UserProfileSerializer

class UserProfileView(APIView):
    """
    Retrieve the profile of the currently logged-in user.
    """
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this endpoint

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)  # Use a dedicated serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
