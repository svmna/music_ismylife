from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('trigger-dag/', views.trigger_airflow_dag, name='trigger_airflow_dag'),
]
