from django.shortcuts import render,HttpResponse, redirect
import datetime
from .models import Posts

def home(request):
    posts = Posts.objects.all()
    content = {
        "posts":posts
    }
    return render(request,'home.html',content)

def about(request):
    return HttpResponse('about')

def blog_post(request,sno):
    post = Posts.objects.filter(sno=sno)
    content2 = {
        "post":post
    }
    print(post)
    return render(request,'full_blog_post.html',content2)