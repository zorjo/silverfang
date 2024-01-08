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
class NoteDetailAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.note = Note.objects.create(user=self.user, title='Test Note', content='This is a test note')

    def test_get_note_detail(self):
        url = reverse('note_detail', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, NoteSerializer(self.note).data)

    def test_get_note_detail_unauthorized(self):
        user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.force_authenticate(user=user2)
        url = reverse('note_detail', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'message': 'You are not authorized to view this note'})

    def test_update_note_detail(self):
        url = reverse('note_detail', args=[self.note.id])
        data = {
            'title': 'Updated Note',
            'content': 'This is an updated note'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, NoteSerializer(self.note).data)

    def test_update_note_detail_unauthorized(self):
        user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.force_authenticate(user=user2)
        url = reverse('note_detail', args=[self.note.id])
        data = {
            'title': 'Updated Note',
            'content': 'This is an updated note'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'message': 'You are not authorized to update this note'})

    def test_delete_note_detail(self):
        url = reverse('note_detail', args=[self.note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Note deleted successfully'})

    def test_delete_note_detail_unauthorized(self):
        user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.force_authenticate(user=user2)
        url = reverse('note_detail', args=[self.note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'message': 'You are not authorized to delete this note'})

class CreateNoteAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_note(self):
        url = reverse('create_note')
        data = {
            'title': 'New Note',
            'content': 'This is a new note'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'New Note')
        self.assertEqual(Note.objects.get().content, 'This is a new note')
        self.assertEqual(Note.objects.get().user, self.user)
        self.assertEqual(response.data, {'id': Note.objects.get().id})
    
    def test_create_note_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('create_note')
        data = {
            'title': 'New Note',
            'content': 'This is a new note'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Note.objects.count(), 0)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})
    
    def test_create_note_invalid_data(self):
        url = reverse('create_note')
        data = {
            'title': '',
            'content': 'This is a new note'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Note.objects.count(), 0)
        self.assertEqual(response.data, {'title': ['This field may not be blank.']})