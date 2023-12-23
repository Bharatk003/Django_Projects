from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    # Query the Question model to get the latest five questions ordered by pub_date in descending order
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    # Create a string by joining the question texts with commas
    output = ",".join([q.question_text for q in latest_question_list])
    
    # Return an HTTP response with the comma-separated list of question texts
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You'are looking at question %s." % question_id)

def results(request, question_id):
    response = "You'are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you'are voting on question %s." % question_id)