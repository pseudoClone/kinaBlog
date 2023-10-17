from django.urls import path
# from . import views
from .views import HomeView,ArticleDetailView, AddPostView

urlpatterns = [
    #path('',views.home,name='home'),
    path('',HomeView.as_view(), name="home"), #as_view returns a callable view that takes request and returns response
    path('article/<int:pk>', ArticleDetailView.as_view(), name = "article-detail"), #int:pk will get the pk of the post
    path('add-post', AddPostView.as_view(), name = 'add_post'),
]
