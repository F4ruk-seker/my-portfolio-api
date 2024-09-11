import time
from django.test import TestCase
from django.test import TestCase
from django.shortcuts import reverse, resolve_url
from django.contrib.auth.models import User
from config.settings import test
from requests import api


class AuthTest(TestCase):
    def setUp(self):
        self.bad_user = User.objects.create_user(
            username='echo',
            password='ratatatata01!',
            email='f4@f4.com'
        )
        # self.bad_user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminadmin!01!',
            email='f22@f4.com',
        )

    def test_bad_user_cant_login_admin_panel(self):
        self.client.login(username='echo', password='ratatatata01!')
        response = self.client.get(reverse('api:custom_admin:page-manage'))
        self.assertEqual(response.status_code, 403)

    def test_jwt_refresh(self):
        self.client.login(username='admin', password='adminadmin!01!')
        test_url = f'{test.MACHINE_IP}{reverse('api:custom_admin:page-manage')}'
        login_url_token = resolve_url(reverse('api:auth:token_obtain_pair'))
        p = api.post(login_url_token, {
            'username': 'echo', 'password': 'ratatatata01!'
        })
        response = self.client.get(reverse('api:custom_admin:page-manage'))
        self.assertEqual(response.status_code, 200)
        time.sleep(2)

        response = self.client.get(reverse('api:custom_admin:page-manage'))
        self.assertEqual(response.status_code, 401)
