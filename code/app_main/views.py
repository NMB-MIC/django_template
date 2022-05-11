from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def main(request):
    return render(request,'app_main/main.html')

def about(request):
    return render(request,'app_main/about.html')