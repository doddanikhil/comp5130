from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

# Create a new note
class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Retrieve and destroy a note after it's read
class NoteRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'access_key'  # Retrieve note by its access key
