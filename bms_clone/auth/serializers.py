from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
from rest_framework.exceptions import ValidationError

User = get_user_model()


# Serializer for User Sign up
class UserSignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
    )
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )
    confirm_password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "confirm_password",
        )

    def validate(self, data):
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        try:
            user = User.objects.filter(email=email)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user:
            raise ValidationError({"error": "Email already exists"})

        if len(username) < 5:
            raise ValidationError({"error": "Username must have minimum 5 characters"})

        if password != confirm_password:
            raise ValidationError({"error": "Passwords mismatch"})

        try:
            user = User.objects.get(username=username)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user:
            raise ValidationError({"error": "Username already exists"})

        return data


# Serializer for User log in
class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
