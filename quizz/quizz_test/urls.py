from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, QuestionsViewSet, QuizzViewSet, ScoresViewSet, QuizzDetails, QuestionsDetails

router = routers.DefaultRouter()
router.register(r'add-quizz', QuizzDetails)
router.register(r'add-questions', QuestionsDetails)
router.register(r'quizz', QuizzViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'scores', ScoresViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]