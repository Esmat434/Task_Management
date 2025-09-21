import uuid

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from .models import (
    PasswordResetToken
)
from .serializers import (
    RegisterSerializer,ProfileSerializer,PasswordResetrequestSerializer,PasswordResetConfirmSerializer,
    ChangePasswordSerializer
)
from .permissions import (
    IsNotAuthenticated
)


User=get_user_model()

class RegisterView(APIView):
    permission_classes = [IsNotAuthenticated]
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail":"Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=ChangePasswordSerializer(
            data=request.data,
            context={'request':request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"detail":"Password changed successfully"}, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetRequestView(APIView):
    permission_classes = [IsNotAuthenticated]
    
    @extend_schema(
        summary="Password Reset Request",
        description=(
            "Creates a password reset token for the user by providing their email. "
            "Important: The token is returned directly in the API response. "
            "The user must use this token when calling PasswordResetConfirm. "
            "The token is not sent via email or any other method."
        ),
        request=PasswordResetrequestSerializer,
        responses={
            201: {"access": "token-uuid"},
            400: {"detail": "Validation errors"}
        }
    )
    def post(self,request):
        serializer = PasswordResetrequestSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.validated_data['email'])
            reset_token,_ = PasswordResetToken.objects.update_or_create(
                user=user,
                defaults={
                    'token':uuid.uuid4(),
                    'created_at':timezone.now()
                }
            )
            return Response({"access":reset_token.token}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    permission_classes = [IsNotAuthenticated]
    
    @extend_schema(
        summary="Password Reset Confirm",
        description=(
            "Resets the user's password using the token generated in PasswordResetRequest. "
            "Provide the reset token and the new password in the request."
        ),
        request=PasswordResetConfirmSerializer,
        responses={
            200: {"detail": "Your password has been successfully reset."},
            400: {"detail": "Validation errors"}
        }
    )
    def post(self,request,uuid):
        token=get_object_or_404(PasswordResetToken, token=uuid)
        serializer=PasswordResetConfirmSerializer(
            data=request.data,
            context={'user':token.user}
        )
        if serializer.is_valid():
            serializer.save()
            token.delete()
            return Response({"detail":"Your password successfully reset."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,username):
        user = get_object_or_404(User, username=username)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,username):
        user = get_object_or_404(User, username=username)
        serializer = ProfileSerializer(data=request.data, instance=user,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
