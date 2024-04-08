import factory

from core.models import User
from exercise.models import Exercise


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    password = factory.Faker('password')

    class Meta:
        model = User


class ExerciseFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    type = factory.Faker('word')
    level = factory.Iterator([choice[0] for choice in Exercise.LEVEL])
    duration = factory.Faker('time_delta')
    repetitions = factory.Faker('sentence', nb_words=4)

    class Meta:
        model = Exercise
