from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()

class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
