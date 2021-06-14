from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSignupSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class TestView(APIView):

    def get(self, request):
        return Response({'info': 'Test View'})


class UserSignupView(APIView):
    """
    View for sign up.
    """
    serializer_class = UserSignupSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            user.is_active = False
            user.save()

            return Response({'info': 'Signup Successful', 'userId': user.id})
        raise ValidationError({'error': 'Invalid User'})
