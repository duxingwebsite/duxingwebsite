from django.forms import ModelForm
from .models import AnswerForQuestion


class AnswerForQuestionForm(ModelForm):
    class Meta:
        model = AnswerForQuestion
        fields = '__all__'

