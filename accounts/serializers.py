import uuid
from django.utils import timezone
from rest_framework import serializers
from .models import (
    CustomUser
)

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields=(
            'username','email','first_name','last_name','date_joined','password',
            'confirm_password'
        )
        extra_kwargs = {
            'password':{'write_only':True},
            'date_joined':{'read_only':True}
        }
    
    def validate_username(self,username):
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username already exists.")
        return username
    
    def validate_email(self,email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email already exists.")
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        
        if len(password)<8:
            raise serializers.ValidationError("Your password must be 8 or more characters.")
        
        if password != confirm_password:
            raise serializers.ValidationError("Your password do not match with confirm password.")
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)    
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = (
            'username','email','first_name','last_name'
        )
    
    def validate_username(self,username):
        if CustomUser.objects.filter(username=username).exclude(id=self.instance.pk).exists():
            raise serializers.ValidationError("This username already exists.")
        return username
    
    def validate_email(self,email):
        if CustomUser.objects.filter(email=email).exclude(id=self.instance.pk).exists():
            raise serializers.ValidationError("This email already exists.")
        return email

class PasswordResetrequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        if not CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"error":"This email does not exists."})
        return attrs

class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']

        if len(password)<8:
            raise serializers.ValidationError("Your password must be 8 or more characters.")
        
        if password != confirm_password:
            raise serializers.ValidationError("Your password do not match with confirm password.")
        
        return attrs
    
    def save(self, **kwargs):
        user=self.context['user']
        user.set_password(self.validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    def validate_old_password(self,value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct.")
        return value

    def validate(self, attrs):

        if len(attrs['new_password'])<8:
            raise serializers.ValidationError("Your password must be 8 or more characters.")
        
        if attrs['new_password'] != attrs['repeat_password']:
            raise serializers.ValidationError("Your password do not match with confirm password")

        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user