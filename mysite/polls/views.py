from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question
# # Create your views here.
# def index(request):
#     # Query the Question model to get the latest five questions ordered by pub_date in descending order
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     templete = loader.get_template("polls/index.html")
#     context  = {
#         "latest_question_list" : latest_question_list,
#     }
#     # Create a string by joining the question texts with commas
#     # output = ",".join([q.question_text for q in latest_question_list])
    
#     # Return an HTTP response with the comma-separated list of question texts
#     return HttpResponse(templete.render(context, request))

#shortcut provided by django
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You'are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you'are voting on question %s." % question_id)