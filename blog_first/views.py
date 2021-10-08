from django.shortcuts import render,HttpResponse, redirect
import datetime

def homepage(request):
    return render(request,'homepage.html')