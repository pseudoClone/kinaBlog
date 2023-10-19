from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView #List in hugo listTemplates and viewTemplate
from .models import Post
from .forms import PostForm
# Will be using class based views from now on

#def home(request):
#    return render(request, 'home.html',{}) # render the request to home.html and point to a dictionary

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__' # This makes the class use all fields from the post model we created
    # Since we use PostForm we will not need field setting

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'editpost.html'
    fields = ['title', 'title_tag', 'body'] # Changing author does not make sense and yes security
