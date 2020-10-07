from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from .serializers.postserializer import PostSerializer
from .serializers.userserializer import RegisterUserSerializer, UserSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer


class UsersView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class AddPostView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request: Request, filename=None):
        file_obj = request.data['file']
        post = Post.objects.create(image=file_obj, owner=request.user)

        return Response({"id": str(post.id)}, status=status.HTTP_201_CREATED)


class AddPostCaptionView(APIView):
    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.caption = request.POST.get("caption")
            post.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllPostsListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("likes")


class LikePostView(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.like(request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UnlikePostView(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.unlike(request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostsListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("likes")
