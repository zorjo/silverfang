#from rest_framework.test import APIRequestFactory
from django.urls import reverse
# Create your tests here.
#create a test for the hello_world view
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class HelloWorldTest(TestCase):
    def test_hello_world(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Hello, World!')


class Integration(TestCase):
    def test_everything(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

        response = self.client.post(reverse("token"), {
            'username': 'testuser',
            'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        token=response.data['token']
        response=self.client.post(reverse('note_create'),headers={'Authorization': 'Token '+token},data={'title':'This is central control','content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat'})
        #Note.objects.create(user=user,title='This is central control',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        response=self.client.get(reverse('search'),{
            'q': 'consectetur adipiscing'},headers={'Authorization': 'Token '+token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        

