import pytest
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise_library.settings')
django.setup()

from rest_framework_simplejwt.tokens import AccessToken
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import UserFactory, ExerciseFactory

register(UserFactory)
register(ExerciseFactory)


@pytest.fixture()
def client() -> APIClient:
    return APIClient()


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture()
def auth_client(client, user) -> APIClient:
    client.force_login(user)
    return client


@pytest.fixture()
def access_token(user):  # Создаем фикстуру для создания JWT-токена
    token = AccessToken.for_user(user)
    return token


@pytest.fixture()
def auth_client_with_token(client, access_token):  # Добавляем токен к клиенту
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))
    return client


@pytest.fixture()
def exercise():
    return ExerciseFactory()
