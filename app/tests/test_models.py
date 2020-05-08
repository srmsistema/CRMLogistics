import datetime
from django.test import TestCase, Client
from crm.app.models import User, Driver, TradingSet
import unittest
from rest_framework.test import APITestCase, APIRequestFactory


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='usertest123',
                                        email='testuser@gmail.com', is_staff=True)

    def test_user_attributes(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@gmail.com')
        self.assertEqual(self.user.status, 'manager')

    def test_user_str(self):
        print(self.user.__str__)
        self.assertEqual(str(self.user), 'testuser')

    def test_login(self):
        login = self.user.login(username='testuser', password='usertest123')


class DriverTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create(username='driver', password='usertest123',
                                        email='driver@gmail.com', is_staff=True)

        self.driver = Driver.objects.create(user='driver', first_name='Daniyar', last_name='Daniyarov',
                                          date_of_birth=datetime.date.today, phone='+996705360090')

    def test_driver_attributes(self):
        self.assertEqual(self.driver.first_name, 'Daniyar')
        self.assertEqual(self.driver.last_name, 'Daniyarov')
        self.assertEqual(self.driver.date_of_birth, datetime.date.today)
        self.assertEqual(self.driver.phone, '+996705260090')

    def test_driver_str(self):
        print(self.driver.__str__)
        self.assertEqual(str(self.driver), 'driver')


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client.objects.create(user='client', first_name='Vanya', last_name='Ivanov',
                                          dateOfBirth=datetime.date.today, phone='+996705360090')

    def test_client_attributes(self):
        self.assertEqual(self.client.first_name, 'Vanya')
        self.assertEqual(self.client.last_name, 'Ivanov')
        self.assertEqual(self.client.dateOfBirth, datetime.date.today)
        self.assertEqual(self.client.phone, '+996705260090')

    def test_client_str(self):
        print(self.client.__str__)
        self.assertEqual(str(self.client), 'client')


class TradingSetTestCase(unittest.TestCase):
    def setUp(self):
        self.trading_set = TradingSet.objects.create(name='Globus', phone='+996705360090',
                                                owner_full_name='Sultanov Nurzhan Syimykovich',
                                          legalAdress='Umetalieva 48-67', IIN='987654876', bankAccount='AB7658765')

    def test_trading_set_attributes(self):
        self.assertEqual(self.trading_set.name, 'Globus')
        self.assertEqual(self.trading_set.phone, '+996705360090')
        self.assertEqual(self.trading_set.owner_full_name, 'Sultanov Nurzhan Syimykovich')
        self.assertEqual(self.trading_set.legalAdress, 'Umetalieva 48-67')
        self.assertEqual(self.trading_set.IIN, '987654876')
        self.assertEqual(self.trading_set.bankAccount, 'AB7658765')

    def test_trading_set_str(self):
        print(self.trading_set.__str__)
        self.assertEqual(str(self.trading_set), 'Globus')