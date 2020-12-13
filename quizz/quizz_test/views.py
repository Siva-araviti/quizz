from django.shortcuts import render
from .models import User, Quizz, Questions,Scores
from .serializers import UserSerializer,QuizzSerializer,QuestionsSerializer,ScoreSerializer
from rest_framework import viewsets, generics, permissions, serializers


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class QuizzDetails(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuizzSerializer
    queryset = Quizz.objects.all()
    http_method_names = ['post']


class QuizzViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = QuizzSerializer
    queryset = Quizz.objects.all()
    http_method_names = ['get','put']


class QuestionsDetails(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    http_method_names = ['post']


class QuestionsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    http_method_names = ['get', 'put']


class ScoresViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ScoreSerializer
    queryset = Scores.objects.all()