from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory

from accounts.serializers import (
    RegisterSerializer,ProfileSerializer,PasswordResetrequestSerializer,PasswordResetConfirmSerializer,
    ChangePasswordSerializer,
)

User=get_user_model()

class TestSerializers(TestCase):
    def setUp(self):
        self.user_instance = User.objects.create_user(username='test',email='test@gmail.com',password='123456789')

    def test_register_serializer(self):
        data = {
            'username':'ali','email':'ali@gmail.com','password':'123456789','confirm_password':'123456789'
        }
        serializer = RegisterSerializer(data=data)
        self.assertEqual(serializer.is_valid(),True)
    
    def test_profile_serializer(self):
        data = {
            'username':'max'
        }
        serializer = ProfileSerializer(data=data, instance=self.user_instance, partial=True)
        self.assertEqual(serializer.is_valid(),True)
    
    def test_password_reset_request_serializer(self):
        data = {
            'email':'test@gmail.com'
        }
        serializer = PasswordResetrequestSerializer(data=data)
        self.assertEqual(serializer.is_valid(),True)
    
    def test_password_reset_confirm_serializer(self):
        data = {
            'password':'Test12345',
            'confirm_password':'Test12345'
        }
        serializer = PasswordResetConfirmSerializer(data=data, context={'user':self.user_instance})
        self.assertEqual(serializer.is_valid(),True)
    
    def test_change_password_serializer(self):
        data = {
            'old_password':'123456789',
            'new_password':'Test12345',
            'repeat_password':'Test12345'
        }

        factory = APIRequestFactory()
        request = factory.post('/fake-url/', data, format='json')
        request.user=self.user_instance

        serializer = ChangePasswordSerializer(data=data, context={'request':request})
        self.assertEqual(serializer.is_valid(),True)