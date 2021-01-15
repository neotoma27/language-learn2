from django.contrib import admin

from .models import User, VocabMCQuestion, VocabMCChoice, Lesson

admin.site.register(User)
admin.site.register(VocabMCQuestion)
admin.site.register(VocabMCChoice)
admin.site.register(Lesson)