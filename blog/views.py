from dataclasses import fields
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
)
from . import views
from .models import Post



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return  render(request, 'blog/home.html',context)

class PostListView(ListView):
    model =Post
    template_name ='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering =['-date_posted']

class PostDetailView(DetailView):
    model =Post
   

class PostCreateView(CreateView):
    model = Post
    #fileds =['title', 'content','cover', 'category']
    fields ='__all__'

def about(request):
    return  render(request, 'blog/about.html',{'title': 'About'})