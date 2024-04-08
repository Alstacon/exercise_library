import pytest
from django.urls import reverse
from rest_framework import status

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer


@pytest.mark.django_db
class TestExercisesList:
    url = reverse('exercises-list')

    def test_get_list(self, auth_client_with_token, exercise_factory):
        exercises = exercise_factory.create_batch(2)

        response = auth_client_with_token.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        for ex in ExerciseSerializer(exercises, many=True).data:
            assert ex in response.data

    def test_unauthorized(self, client):
        response = client.get(self.url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_filtering_by_level(self, auth_client_with_token, exercise_factory):
        for level in ['HARD', 'MEDIUM', 'EASY']:
            exercise_factory.create_batch(2, level=level)

        response = auth_client_with_token.get(self.url, {'level': 'EASY'})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ExerciseSerializer(Exercise.objects.filter(level='EASY'), many=True).data

        response = auth_client_with_token.get(self.url, {'level': 'HARD'})
        assert response.status_code == status.HTTP_200_OK
        assert not response.json() == ExerciseSerializer(Exercise.objects.all(), many=True).data
