from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User=get_user_model()

class TestPermissions(TestCase):
    def setUp(self):
        self.user_instance = User.objects.create_user(username='test',email='test@gmail.com',password='12345678')
        self.data = {
            'username':'ali','email':'ali@gmail.com','password':'123456789','confirm_password':'123456789'
        }   

    def test_login_required_mixin(self):
        self.client.force_login(self.user_instance)
        url = reverse('accounts:profile', args=[self.user_instance.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_logout_required_mixin(self):
        url = reverse('accounts:register')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code,201)