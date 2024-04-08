from django.db import models


class Exercise(models.Model):
    LEVEL = (
        ('HARD', 'Продвинутый'),
        ('MEDIUM', 'Средний'),
        ('EASY', 'Для начинающих')
    )
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    type = models.CharField(max_length=100, verbose_name='Тип')
    level = models.CharField(choices=LEVEL, verbose_name='Уровень сложности')
    duration = models.DurationField(verbose_name='Продолжительность выполнения')
    repetitions = models.CharField(max_length=255, verbose_name='Рекомендуемый набор повторений и подходов')

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.name
