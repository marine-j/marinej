from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def home(request):
	return render(request, 'pomodoro/pomodoro.html')

def about(request):
	return render(request, 'pomodoro/about.html')