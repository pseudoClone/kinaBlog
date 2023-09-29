from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html') #The template is the index.html

def contact(request):
    return render(request, 'core/contact.html')
