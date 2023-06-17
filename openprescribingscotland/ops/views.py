from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello world, this is Isi!")
    # return render(request, "ops/home.html") # Eventually use HTML template