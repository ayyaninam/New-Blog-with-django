from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name="Homepage"),
    path('about/', views.about, name="about"),
    path('blog-post/<int:sno>', views.blog_post, name="blog_post"),
]