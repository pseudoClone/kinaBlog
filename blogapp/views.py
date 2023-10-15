from django.shortcuts import render
from django.views.generic import ListView, DetailView #List in hugo listTemplates and viewTemplate
from .models import Post
# Will be using class based views from now on

#def home(request):
#    return render(request, 'home.html',{}) # render the request to home.html and point to a dictionary

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
