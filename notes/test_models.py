from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a note for testing
        cls.note = Note.objects.create(
            user=cls.user,
            title='Test Note',
            content='This is a test note',
            search_vector='test search vector'
        )

    def test_user_foreign_key(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.user, self.user)

    def test_title_max_length(self):
        note = Note.objects.get(id=self.note.id)
        max_length = note._meta.get_field('title').max_length
        self.assertLessEqual(len(note.title), max_length)

    def test_content_not_empty(self):
        note = Note.objects.get(id=self.note.id)
        self.assertNotEqual(note.content, '')

    def test_search_vector_null_blank(self):
        note = Note.objects.get(id=self.note.id)
        self.assertIsNone(note.search_vector)
        self.assertTrue(note._meta.get_field('search_vector').blank)

    # Add more tests as needed