import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    display_name = models.CharField(max_length=50)
    email = models.EmailField()
    join_date = models.DateTimeField(auto_now_add=True)
    knowledge_points = models.IntegerField(default=0)
    energy_fruits = models.IntegerField(default=2)
    def __str__(self):
        return self.username

class Lesson(models.Model):
    subject = models.CharField(max_length=30)

class VocabMCQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='question_set')
    first_language_word = models.CharField(max_length=40)
    target_language_word = models.CharField(max_length=40)

class VocabMCChoice(models.Model):
    question = models.ForeignKey(VocabMCQuestion, on_delete=models.CASCADE, related_name='choice_set')
    word_choice = models.CharField(max_length=40)