from django.urls import path, include
from django.contrib import admin
from rest_framework import generics, permissions, serializers
from .models import User,Quizz,Questions,Scores
admin.autodiscover()


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class QuizzSerializer(serializers.ModelSerializer):


    class Meta:
        model = Quizz
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass
    options = serializers.ListField()

    def update(self, instance, validated_data):
        request = self.context.get('request')
        answer = validated_data.get('answer','')
        quizz_id = validated_data.get('quiz_id','')
        option = validated_data.get('option', '')
        if option == answer:
            previous_score = Scores.objects.get(user_id=request.user, quizz_id=quizz_id)
            if previous_score:
                score = previous_score + 1
                Scores.objects.create(user_id=request.user, quizz_id=quizz_id, score = score)

    class Meta:
        model = Questions
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scores
        fields = '__all__'