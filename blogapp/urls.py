from django.urls import path
# from . import views
from .views import HomeView

urlpatterns = [
    #path('',views.home,name='home'),
    path('',HomeView.as_view(), name="home"), #as_view returns a callable view that takes request and returns response
]
