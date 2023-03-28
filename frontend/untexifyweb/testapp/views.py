from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(content="This is the index!")


def quadratic(request, x):
    output = x ** 2
    return HttpResponse(output)
