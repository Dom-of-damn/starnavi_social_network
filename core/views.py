from activity_log.models import ActivityLog
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.analytics import get_like_analytics
from core.models import User, Post, PostsFeedBack
from core.serializers import (
    UserSerializer,
    PostSerializer,
    PostsFeedBackSerializer,
    FeedbackAnalyticsSerializer,
    UserActivitySerializer
)


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


class FeedbackAnalyticsApiView(APIView):
    """
    Implements feedback analytics of users posts feedback in
    range(date_from,date_to)
    """
    serializer_class = FeedbackAnalyticsSerializer

    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        data = get_like_analytics(date_from, date_to)
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class UserActivityApiView(APIView):
    """
    Implements getting user activity by email of user.
    """
    serializer_class = UserActivitySerializer

    def get(self, request):
        user_email = request.query_params.get('email')
        try:
            user = User.objects.get(email=user_email)
        except User.DoesNotExist:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {
                'last_login': user.last_login,
                'last_response': ActivityLog.objects.filter(user=user).last()
            }
            print(data)
            serializer = self.serializer_class(data)
            return Response(serializer.data)
