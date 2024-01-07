from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ['id', 'title', 'content', 'user']
    read_only_fields = ['user']
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "username"]

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  class Meta:
    model = User
    fields = ('username', 'password', 'email')

 #   return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
