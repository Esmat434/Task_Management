import uuid
from django.urls import reverse
from django.test import TestCase

class TestUrls(TestCase):
    def test_token_url(self):
        url = reverse('accounts:token_obtain_pair')
        self.assertEqual(url,'/api/token/')
    
    def test_refresh_token_url(self):
        url = reverse('accounts:token_refresh')
        self.assertEqual(url,'/api/token/refresh/')

    def test_register_url(self):
        url = reverse('accounts:register')
        self.assertEqual(url,'/api/register/')
    
    def test_logout_url(self):
        url = reverse('accounts:logout')
        self.assertEqual(url,'/api/logout/')
    
    def test_password_reset_request(self):
        url = reverse('accounts:password_reset_request')
        self.assertEqual(url,'/api/password_reset_request/')
    
    def test_password_reset_confirm(self):
        token = uuid.uuid4()
        url = reverse('accounts:password_reset_confirm', args=[token])
        self.assertEqual(url,f'/api/password_reset_confirm/{token}/')
    
    def test_change_password(self):
        url = reverse('accounts:change_password')
        self.assertEqual(url,'/api/change_password/')
    
    def test_profile_url(self):
        url = reverse('accounts:profile', args=['ali'])
        self.assertEqual(url,'/api/profile/ali/')