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

class CreateUserTest(TestCase):
    def test_create_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'abc@xyz.com',
            'password': 'testpass123'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'abc@xyz.com')

class NoteTestSearch(TestCase):
    def test_token(self):
        user=User.objects.create(username='testuser',
        email='abc@xyz.com'
    )
        user.set_password('testpass123')
        user.save()
        response = self.client.post(reverse("token"), {
            'username': 'testuser',
            'password': 'testpass123'})
        self.assertEqual(response.status_code, 200)
        token=response.data['token']
        Note.objects.create(user=user,title='This is central control',content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat')
        response=self.client.get(reverse('search'),{
            'q': 'consectetur adipiscing'},headers={'Authorization': 'Token '+token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        """
        response=self.client.get(reverse('details'),headers={'Authorization': 'Token '+token})
        self.assertEqual(response.status_code, 200)
        response=self.client.post(reverse('note_create'),{
            'title': 'testtitle',
            'content':"testcontent"},headers={'Authorization': 'Token '+self.token})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['title'], 'testtitle')
        self.assertEqual(response.data['content'], 'testcontent')
        """


class CreateNoteTest(TestCase):
    def setUp(self):
        def test_create_user_and_note(self):
            response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'a@b.com',
            'password': 'testpass123'})
            self.assertEqual(response.status_code, 201)
            response = self.client.post(reverse('token'), {
            'username': 'testuser',
            'password': 'testpass123'})
            self.assertEqual(response.status_code, 200)
            self.token=response.data['token']
            response=self.client.post(reverse('note_create'),{
            'title': 'testtitle',
            'content':"testcontent"},headers={'Authorization': 'Token '+self.token})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['id'], 1)
            self.assertEqual(response.data['title'], 'testtitle')
            self.assertEqual(response.data['content'], 'testcontent')

