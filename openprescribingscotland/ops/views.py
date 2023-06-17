from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "ops/index.html")
    # return render(request, "ops/home.html") # Eventually use HTML template