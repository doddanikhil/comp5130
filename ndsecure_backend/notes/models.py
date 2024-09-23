import uuid
from django.db import models

class Note(models.Model):
    content = models.TextField()  # This stores the encrypted content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation time
    expires_at = models.DateTimeField(null=True, blank=True)  # Optional expiration time
    access_key = models.CharField(max_length=50, unique=True, blank=True)  # Unique access key for each note
    has_been_read = models.BooleanField(default=False)  # Indicates if the note has been read

    def save(self, *args, **kwargs):
        if not self.access_key:
            self.access_key = str(uuid.uuid4())  # Generate a unique access key using uuid
        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.access_key  # Returns the access key as the string representation of the note
