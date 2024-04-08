from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from exercise import serializers, models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ExercisesViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для работы с моделью упражнений
    """
    queryset = models.Exercise.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.ExerciseSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('level', 'type')
    ordering_fields = ('id',)
    ordering = ('id',)
