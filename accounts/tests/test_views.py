import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from accounts.models import (
    PasswordResetToken
)

User = get_user_model()

class TestRegisterView(TestCase):
    def setUp(self):
        self.data = {
            'username':'test','email':'test@gmail.com','password':'123456789',
            'confirm_password':'123456789'
        }
    
    def test_post_method(self):
        url = reverse('accounts:register')
        response = self.client.post(url, data=self.data)
        
        self.assertEqual(response.status_code, 201)

class TestLogoutView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',email='test@gmail.com',password='123456789'
        )
        self.client = APIClient()
        self.client.force_login(self.user)
    
    def test_logout(self):
        refresh = RefreshToken.for_user(self.user)
        refresh_token = str(refresh)

        url = reverse('accounts:logout')
        response = self.client.post(url, {'refresh':refresh_token}, format='json')

        self.assertEqual(response.status_code, 200)

class TestChangePasswordView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',email='test@gmail.com',password='123456789'
        )
        self.client.force_login(self.user)
        self.data = {
            'old_password':'123456789',
            'new_password':'test12345%',
            'repeat_password':'test12345%'
        }

    def test_post_method(self):
        url = reverse('accounts:change_password')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 200)

class TestPasswordResetRequestView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',email='test@gmail.com',password='123456789'
        )
        self.data = {
            'email':self.user.email
        }
    
    def test_post_method(self):
        url = reverse('accounts:password_reset_request')
        response = self.client.post(url, data=self.data)

        self.assertEqual(response.status_code, 201)

class TestPasswordResetConfirmView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@gmail.com', password='123456789'
        )
        self.token_instance = PasswordResetToken.objects.create(user=self.user)
        self.data = {
            'password':'test123456',
            'confirm_password':'test123456'
        }
    
    def test_post_method(self):
        url = reverse('accounts:password_reset_confirm', args=[self.token_instance.token])
        response = self.client.post(url, data=self.data)

        self.assertEqual(response.status_code, 200)

class TestProfileView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@gmail.com', password='test12345'
        )
        self.client.force_login(self.user)
        self.data = {
            'username':'alex'
        }
    
    def test_get_method(self):
        url = reverse('accounts:profile', args=[self.user.username])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
    def test_put_method(self):
        url = reverse('accounts:profile', args=[self.user.username])
        response = self.client.put(
            url, 
            data=json.dumps(self.data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)