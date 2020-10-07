import uuid

from django.contrib.auth import get_user_model
from django.db import models, IntegrityError
from django.utils import timezone

UserModel = get_user_model()


def uploaded_image_name(instance, filename):
    """Makes file name unique."""
    return "{}{}".format(str(instance.id), filename)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to=uploaded_image_name)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="posts")
    caption = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def liked_by(self):
        return PostLikes.objects.filter(post=self)

    def __str__(self):
        return self.image.url

    def like(self, user):
        try:
            PostLikes.objects.create(post=self, user=user)
        except IntegrityError:
            pass

    def unlike(self, user):
        try:
            PostLikes.objects.get(post=self, user=user).delete()
        except PostLikes.DoesNotExist:
            pass


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="liked_posts")

    class Meta:
        unique_together = ["post", "user"]

    def __str__(self):
        return self.user.get_username()
