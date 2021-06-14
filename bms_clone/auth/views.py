from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSignupSerializer, UserLoginSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from django.contrib.auth import login, authenticate, logout


def get_tokens_for_user(user):
    """
    function to get access, refresh tokens
    """
    refresh = RefreshToken.for_user(user)
    refresh.payload["sub"] = user.id
    refresh.payload["iat"] = datetime.now()
    refresh.access_token.payload["sub"] = user.id
    refresh.access_token.payload["iat"] = datetime.now()
    return str(refresh), str(refresh.access_token)


class UserSignupView(APIView):
    """
    View for sign up.
    """

    serializer_class = UserSignupSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]
            email = serializer.validated_data["email"]
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )

            # user.is_active = False
            user.save()

            refresh, access = get_tokens_for_user(user)

            return Response(
                {
                    "info": "Signup Successful",
                    "userId": user.id,
                    "refresh": refresh,
                    "access": access,
                }
            )
        raise ValidationError({"error": "Invalid User"})


class UserLoginView(APIView):
    """
    View for log in.
    """

    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                refresh, access = get_tokens_for_user(user)
                login(request, user)
                return Response(
                    {"info": "Successful login", "refresh": refresh, "access": access}
                )
            return Response({"error": "User not verified"})
        return Response({"error": "Invalid Credentials"})


class HomeView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response({"info": "Welcome to BMS"})
