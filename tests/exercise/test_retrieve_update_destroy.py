import pytest
from django.urls import reverse
from rest_framework import status

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer


@pytest.mark.django_db
class TestExerciseRetrieve:
    def test_retrieve(self, auth_client_with_token, user, exercise):
        url = reverse('exercises-detail', args=[exercise.id])
        response = auth_client_with_token.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ExerciseSerializer(exercise).data

    def test_get_unauthorized(self, client):
        url = reverse('exercises-detail', args=[1])

        response = client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestUpdateExercise:
    def test_update_success(self, auth_client_with_token, exercise):
        url = reverse('exercises-detail', args=[exercise.id])

        response = auth_client_with_token.patch(url, data={'name': 'New name'})

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == 'New name'

    def test_update_unauthorized(self, client):
        url = reverse('exercises-detail', args=[1])

        response = client.patch(url, data={'name': 'New name'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestDestroyExercise:
    def test_destroy_success(self, auth_client_with_token, exercise):
        url = reverse('exercises-detail', args=[exercise.id])
        exercise_id = exercise.id
        response = auth_client_with_token.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Exercise.objects.filter(id=exercise_id)

    def test_destroy_unauthorized(self, client):
        url = reverse('exercises-detail', args=[1])

        response = client.delete(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
