import uuid
from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_user = models.ForeignKey(User, related_name="first_user", on_delete=models.CASCADE)
    second_user = models.ForeignKey(User, related_name="second_user", on_delete=models.CASCADE)


class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

