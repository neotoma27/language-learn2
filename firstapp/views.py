from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User, VocabMCQuestion, VocabMCChoice


def index(request):
    user = get_object_or_404(User, pk='emmycat')
    return render(request, 'firstapp/index.html', {'user': user})

class HighscoresView(generic.ListView):
    template_name = 'firstapp/highscores.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.order_by('-knowledge_points')

class ProfileView(generic.DetailView):
    model = User
    template_name = 'firstapp/profile.html'

def vocabmcquestion(request, question_id):
    user = get_object_or_404(User, pk='emmycat')
    question = get_object_or_404(VocabMCQuestion, pk=question_id)
    return render(request, 'firstapp/vocabmcquestion.html', {'user': user, 'question': question})

def answerquestion(request, question_id):
    question = get_object_or_404(VocabMCQuestion, pk=question_id)
    user = get_object_or_404(User, pk='emmycat')
    if request.POST['choice'] == question.target_language_word:
        user.knowledge_points += 4
        user.save()
        if question.id >= question.lesson.question_set.count():
            user.knowledge_points += 6
            user.save()
            return HttpResponseRedirect('/firstapp/lessoncomplete/')
        else:
            return HttpResponseRedirect(reverse('firstapp:question', args=((question.id + 1),)))
    else:
        if user.energy_fruits <= 1:
            user.energy_fruits = 2
            user.save()
            return render(request, 'firstapp/vocabmcquestion.html', {
                'question': question,
                'user': user,
                'feedback_message': "Answer incorrect. You ran out of Energy Fruits. Your Energy Fruits have been refilled.",
            })
        else:
            user.energy_fruits -= 1
            user.save()
            return render(request, 'firstapp/vocabmcquestion.html', {
                'question': question,
                'user': user,
                'feedback_message': "Answer incorrect.",
            })

def lessoncomplete(request):
    return render(request, 'firstapp/lessoncomplete.html', {})