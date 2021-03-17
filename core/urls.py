from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    CreateUserView,
    CreatePostView,
    ListPostView,
    PostsFeedbackUpdateDestroyAPIView,
    PostsFeedbackListCreateAPIView,
    FeedbackAnalyticsApiView,
    UserActivityApiView
)

urlpatterns = [
    path('api/analytics/', FeedbackAnalyticsApiView.as_view(), name='analytics'),
    path('api/post/create/', CreatePostView.as_view(), name='create_post'),
    path('api/post/list/', ListPostView.as_view(), name='post_list'),
    path('api/post/feedback/', PostsFeedbackListCreateAPIView.as_view(), name='feedback_get_or_create'),
    path('api/post/feedback/<pk>/', PostsFeedbackUpdateDestroyAPIView.as_view(), name='feedback_update_or_destroy'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/create/', CreateUserView.as_view(), name='create_user'),
    path('api/user/activity/', UserActivityApiView.as_view(), name='user_activity'),
]
