from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from core.serializers import CreateUserSerializer, PasswordUpdateSerializer


class CreateUserView(CreateAPIView):
    """
    Регистрация пользователя
    """
    serializer_class = CreateUserSerializer


class PasswordUpdateView(UpdateAPIView):
    """
    Замена пароля
    """
    serializer_class = PasswordUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
