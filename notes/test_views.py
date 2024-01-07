from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Note
from .serializers import NoteSerializer

class SearchAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.note1 = Note.objects.create(user=self.user, title='Test Note 1', content='This is a test note 1')
        self.note2 = Note.objects.create(user=self.user, title='Test Note 2', content='This is a test note 2')
        self.note3 = Note.objects.create(user=self.user, title='Another Note', content='This is another note')

    def test_search_with_query(self):
        url = reverse('search')
        query = 'test'
        response = self.client.get(url, {'q': query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = NoteSerializer([self.note1, self.note2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_search_without_query(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'No query was provided'})

    def test_search_with_no_results(self):
        url = reverse('search')
        query = 'nonexistent'
        response = self.client.get(url, {'q': query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_search_with_different_user(self):
        user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.force_authenticate(user=user2)
        url = reverse('search')
        query = 'test'
        response = self.client.get(url, {'q': query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
class ShowNotesAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.note1 = Note.objects.create(user=self.user, title='Test Note 1', content='This is a test note 1')
        self.note2 = Note.objects.create(user=self.user, title='Test Note 2', content='This is a test note 2')
        self.note3 = Note.objects.create(user=self.user, title='Another Note', content='This is another note')

    def test_show_notes(self):
        url = reverse('notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = NoteSerializer([self.note1, self.note2, self.note3], many=True).data
        self.assertEqual(response.data, expected_data)
class RegisterUserAPIViewTest(APITestCase):
    def test_register_user(self):
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