from django.urls import path
from . import views
app_name = 'item' #Say that this is a namespace, but idk

urlpatterns = [
        path('<int:pk>/', views.detail, name = 'detail'),
        ]
