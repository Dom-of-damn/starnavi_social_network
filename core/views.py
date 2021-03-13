from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    queryset = User
    serializer_class = UserSerializer
