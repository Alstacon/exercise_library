from rest_framework.routers import SimpleRouter
from django.urls import include, path

from exercise import views

router = SimpleRouter()

router.register('exercises', views.ExercisesViewSet, basename='exercises')
# router.register('group', views.StudentGroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
