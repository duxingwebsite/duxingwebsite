from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Question
from .forms import AnswerForQuestionForm


def index(request):
    return render(request, 'recruitment/index.html')


def thanks(request):
    return render(request, 'recruitment/thanks.html')


class QuestionView(ListView):
    model = Question
    template_name = "recruitment/question.html"
    context_object_name = "question_list"
    paginate_by = 50

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)


class CreateAnswerView(CreateView):
    form_class = AnswerForQuestionForm
    template_name = 'recruitment/answer_form.html'
    success_url = '/recruitment/thanks'

    def form_invalid(self, form):
        return render(self.request, 'recruitment/invalid.html')


