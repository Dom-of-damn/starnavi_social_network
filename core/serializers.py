from activity_log.models import ActivityLog
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models import User, Post, PostsFeedBack


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        """
        If don't implement, password will be not hashing
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post


class PostsFeedBackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PostsFeedBack
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = validated_data['post']
        try:
            PostsFeedBack.objects.get(user=user, post_id=post_id)
            raise serializers.ValidationError(
                f'Feedback exists for post with id:"{post_id}" and user:"{user}"!'
            )
        except PostsFeedBack.DoesNotExist:
            post = PostsFeedBack.objects.create(user=user, **validated_data)
            return post


class FeedbackAnalyticsSerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    count = serializers.IntegerField()


class ResponseActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ['request_url', 'request_method', 'response_code', 'datetime']


class UserActivitySerializer(serializers.Serializer):
    last_login = serializers.DateTimeField()
    last_response = ResponseActivityLogSerializer()
