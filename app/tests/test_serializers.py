import datetime
from django.test import TestCase, Client
from crm.app.models import User, Driver, TradingSet
import unittest
from rest_framework.test import APITestCase, APIRequestFactory

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='usertest123',
                                        email='testuser@gmail.com', is_staff=True)

    def setUp(self):
        self.bike_attributes = {
            'color': 'yellow',
            'size': Decimal('52.12')
        }

        self.serializer_data = {
            'color': 'black',
            'size': 51.23
        }

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.bike)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['color', 'size']))

    def test_user_attributes(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@gmail.com')
        self.assertEqual(self.user.status, 'manager')

    def test_user_str(self):
        print(self.user.__str__)
        self.assertEqual(str(self.user), 'testuser')

    def test_login(self):
        login = self.user.login(username='testuser', password='usertest123')