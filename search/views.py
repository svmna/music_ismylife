from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'search/index.html')

def result(request):
    return HttpResponse("이곳은 검색결과가 나와야 합니다...")