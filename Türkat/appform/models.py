from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  # image = models.ImageField(upload_to="Post-Image")
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name="Beğenenler")
    post_save = models.ManyToManyField(User, related_name = "Kaydedenler")
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  # image = models.ImageField(upload_to="Profile-Image")  */
    bio = models.TextField()

class Takip(models.Model):
    profil = models.ForeignKey(Profile, related_name="takipçi_profil", on_delete=models.CASCADE)
    takip_edilen = models.ForeignKey(Profile, related_name="takip_edilen", on_delete=models.CASCADE)

class Takipçi(models.Model):
    profil = models.ForeignKey(Profile, related_name="takip_profil", on_delete=models.CASCADE)
    takip_eden = models.ForeignKey(Profile, related_name="takip_eden", on_delete=models.CASCADE)