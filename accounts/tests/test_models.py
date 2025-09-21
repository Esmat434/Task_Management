from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models import (
    PasswordResetToken
)

User=get_user_model()

class TestModels(TestCase):
    def setUp(self):
        self.user_instance=User.objects.create_user(username='test',email='test@gmail.com')
        self.token = PasswordResetToken.objects.create(user=self.user_instance)
    
    def test_customuser_model(self):
        user=User.objects.get(id=1)
        self.assertEqual(self.user_instance,user)
    
    def test_password_reset_token_model(self):
        self.assertEqual(self.token.user,self.user_instance)
