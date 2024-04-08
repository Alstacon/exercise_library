import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestCreateExercise:
    url = reverse('exercises-list')

    def test_create_success(self, auth_client_with_token):
        data = {
            "name": "Наклоны",
            "description": "Наклониться вперед",
            "type": "Базовое",
            "level": "EASY",
            "duration": "00:01:00",
            "repetitions": "4 подхода по 10 раз"
        }

        response = auth_client_with_token.post(self.url, data=data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_unauthorized(self, client, faker):
        response = client.post(self.url, data=faker.pydict(1))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_invalid_data(self, auth_client_with_token):
        response = auth_client_with_token.post(self.url, data={
            "name": "Наклоны",
            "description": "Наклониться вперед",
            "type": "Базовое",
            "level": "EASY",
            "duration": "40 минут",
            "repetitions": "4 подхода по 10 раз"
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
