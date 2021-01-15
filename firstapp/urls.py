from django.urls import path

from . import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('highscores/', views.HighscoresView.as_view(), name='highscores'),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name='profile'),
    path('question/<int:question_id>/', views.vocabmcquestion, name='question'),
    path('<int:question_id>/answerquestion/', views.answerquestion, name='answerquestion'),
    path('lessoncomplete/', views.lessoncomplete, name='lessoncomplete')
]