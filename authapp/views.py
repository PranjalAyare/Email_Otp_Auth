from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from .models import User, OTP
from .serializers import RegisterSerializer, OTPRequestSerializer, OTPVerifySerializer
from .utils import generate_otp
from .tokens import get_tokens_for_user
import sys
# 🔒 Rate Limiting for OTP Request
class OTPThrottle(UserRateThrottle):
    rate = '3/min'  # Limit to 3 OTP requests per minute per user

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({"message": "Email already registered."}, status=400)
            User.objects.create(email=email)
            return Response({"message": "Registration successful. Please verify your email."})
        return Response(serializer.errors, status=400)

class RequestOTPView(APIView):
    throttle_classes = [OTPThrottle]  # 🚨 Apply the rate limit here

    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                print(f"DEBUG: User found for email: {email}") 
                sys.stdout.flush()
                otp_code = generate_otp()
                OTP.objects.create(user=user, code=otp_code)
                print(f"OTP for {email}: {otp_code}")  # Mock email output
                sys.stdout.flush()
                return Response({"message": "OTP sent to your email."})
            except User.DoesNotExist:
                return Response({"message": "User not found."}, status=404)
        return Response(serializer.errors, status=400)

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email)
                otp_obj = OTP.objects.filter(user=user, code=otp).last()
                if otp_obj and not otp_obj.is_expired():
                    user.is_verified = True
                    user.save()
                    token = get_tokens_for_user(user)
                    return Response({"message": "Login successful.", "token": token})
                return Response({"message": "Invalid or expired OTP."}, status=400)
            except User.DoesNotExist:
                return Response({"message": "User not found."}, status=404)
        return Response(serializer.errors, status=400)
# This code provides the views for user registration, OTP request, and OTP verification in a Django REST framework application.
# It includes rate limiting for OTP requests to prevent abuse.
