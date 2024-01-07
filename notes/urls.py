from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("hello", views.hello_world, name="index"),
    path("auth/signup", views.RegisterUserAPIView.as_view(), name="register"),
    path("auth/token", obtain_auth_token,name="token"),
    path("notes/<int:idx>",views.note_detail, name="note" ),
    path("notes/create",views.create_note, name="note_create"),
    path("notes",views.sho_notes, name="notes" ),
    path("notes/search",views.search, name="search" ),
]