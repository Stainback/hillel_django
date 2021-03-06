from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionListSerializer, QuestionDetailsSerializer, ChoiceListSerializer, \
    ChoiceDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!!!!")


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer


class ChoiceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceDetailsSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))