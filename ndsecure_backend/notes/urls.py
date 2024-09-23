from django.urls import path
from .views import NoteCreateView, NoteRetrieveView

urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='create-note'),  # URL to create a new note
    path('note/<str:access_key>/', NoteRetrieveView.as_view(), name='view-note'),  # URL to retrieve a note by access_key
]
