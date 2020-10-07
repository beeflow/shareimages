from rest_framework import serializers

from api.serializers.userserializer import UserSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    likes = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        instance.caption = validated_data.get("caption", instance.caption)
        instance.save()
        return instance

    def get_likes(self, instance):
        return instance.liked_by.count()

    class Meta:
        model = Post
        fields = "__all__"
        depth = 1
