from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import requests
from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # CSRF 방지를 비활성화 (외부 요청에서만 사용, 보안 문제 고려)
def trigger_airflow_dag(request):
    if request.method == "POST":
        input_value = request.POST.get("input_value")  # form-data에서 key값 가져오기

        if not input_value:
            return JsonResponse({"error": "No input_value provided"}, status=400)

        airflow_url = "http://localhost:8080/api/v1/dags/example_trigger_dag/dagRuns"
        username = 'airflow'
        password = 'airflow'

        payload = {
            "conf": {"input_value": input_value}
        }

        headers = {
            'Content-Type': 'application/json',  # 요청 본문 형식을 JSON으로 설정
            'Accept': 'application/json',         # 응답 형식도 JSON으로 설정
        }

        try:
            response = requests.post(airflow_url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))

            if response.status_code == 200:
                return JsonResponse({"message": "DAG triggered successfully!"})
            else:
                return JsonResponse({"error": response.json()}, status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def index(request):
    return render(request, 'search/index.html')

def result(request):    
    # 모든 데이터 가져오기
    youtube_videos = YouTubeVideo.objects.all()
    youtube_playlists = YouTubePlaylist.objects.all()
    spotify_playlists = SpotifyPlaylist.objects.all()

    # 템플릿으로 데이터 전달
    context = {
        'youtube_videos': youtube_videos,
        'youtube_playlists': youtube_playlists,
        'spotify_playlists': spotify_playlists,
    }
    return render(request, 'search/result.html', context)