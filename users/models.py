from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def follow(self, user):
        Followers.objects.create(user=self, follow=user)

    @property
    def followers(self):
        return Followers.objects.filter(follow=self)

    @property
    def followed(self):
        return Followers.objects.filter(user=self)


class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ("user", "follow")

    def __str__(self):
        return self.user.get_username()
