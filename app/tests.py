from django.test import TestCase
from .models import Password
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.models import User
import json


class PasswordTestCase(TestCase):
    def test_create_password(self):
        Password(username="NeoSahadeo", email="neosahadeo@protonmail.com", nickname="Dummy", password="Password@1234", site_url="localhost", site_name="Local Host the site", notes="This is a dummy login detail to test the password creation").save()
        match = Password.objects.filter(Q(nickname__iexact="Dummy") | Q(nickname__icontains="mmy"))
        for x in match:
            self.assertEqual(x.username, "NeoSahadeo")


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("NeoSahadeo", "", "Password@1234")
        user.save()

    def test_login(self):
        response = self.client.post(reverse('login'), data={
            'username': 'NeoSahadeo',
            'password': 'Password@1234'
        })
        self.assertNotEqual(json.loads(response.content).get('token'), None)


class PasswordUseTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("NeoSahadeo", "", "Password@1234")
        user.save()
        response = self.client.post(reverse('login'), data={
            'username': 'NeoSahadeo',
            'password': 'Password@1234'
        })
        self.token = json.loads(response.content).get('token')

    # Doesnt work for some reason
    # def test_password_get(self):
    #     response = self.client.get(reverse('passwords'), **{
    #         'Authorization': f'Token 78df76d6d4858484112b566c9345f6bd5249ca40f3701edfa99a1477b546643e',
    #     })
    #
    #     print(response.content)
