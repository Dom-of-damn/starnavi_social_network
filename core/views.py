from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import User, Post, PostsFeedBack
from core.serializers import UserSerializer, PostSerializer, PostsFeedBackSerializer


class CreateUserView(CreateAPIView):
    queryset = User
    serializer_class = UserSerializer


class CreatePostView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post
    serializer_class = PostSerializer


class ListPostView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsFeedbackListCreateAPIView(ListCreateAPIView):
    """
    Implement view for creating feedback and get
    feedbacks equal query params or all
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostsFeedBackSerializer

    def get_queryset(self):
        queryset = PostsFeedBack.objects.all()
        post_id = self.request.query_params.get('post_id', None)
        if post_id is not None:
            queryset = queryset.filter(post=post_id)
        return queryset


class PostsFeedbackUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Implement detail get, update(put and patch) and delete
    methods
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostsFeedBackSerializer
    queryset = PostsFeedBack.objects.all()
