#from django.shortcuts import render
from django.contrib.postgres.search import SearchVector
from rest_framework.permissions import IsAuthenticated,AllowAny
#from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Q
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.response import Response
from .models import Note
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer,RegisterSerializer,NoteSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    """
    API endpoint that returns a simple 'Hello, World!' message.
    """
    return Response({'message': 'Hello, World!'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sho_notes(request):
    """
    API endpoint that displays notes.
    """

    notes=Note.objects.filter(user=request.user)
    serializer = NoteSerializer(notes, many=True)
    #user = User.objects.get(id=request.user.id)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note(request):
    """
    API endpoint that creates a new note.
    """
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        note=serializer.save(user=request.user)
        return Response({'id': note.id}, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def sho_user(request):
    """
    API endpoint that displays current user.
    """
    permission_classes = (IsAuthenticated,)
    #user = User.objects.get(id=request.user.id)
    return Response(request.user.email)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_note_by_id(request,idx):
    """
    API endpoint that displays note by id.
    """
    note = get_object_or_404(Note,id=idx)
    serializer = NoteSerializer(note)
    if note.user==request.user:
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def user_detail(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):
    """
    API endpoint that searches for posts by a query string.
    """
    query = request.query_params.get('q', None)
    if query is None:
        return Response({'message': 'No query was provided'})
    #notes = Note.objects.filter(Q(title__icontains=query) | Q(content__icontains=query), user=request.user)
    notes = Note.objects.annotate(search=SearchVector("title", "content")).filter(search=query)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
    