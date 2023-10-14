from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html',{}) # render the request to home.html and point to a dictionary
