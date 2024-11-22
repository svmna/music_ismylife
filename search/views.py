from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("이곳은 검색창만 덩그러니 놓인 첫 화면이 될 것입니다...")

def result(request):
    return HttpResponse("이곳은 검색결과가 나와야 합니다...")