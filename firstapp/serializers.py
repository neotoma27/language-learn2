from django.contrib.auth.models import User, Lesson, VocabMCQuestion, VocabMCChoice
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'display_name', 'email', 'join_date', 'knowledge_points', 'energy_fruits']

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['subject']

class VocabMCQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VocabMCQuestion
        fields = ['lesson', 'first_language_word', 'target_language_word']

class VocabMCChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VocabMCChoice
        fields = ['question', 'word_choice']