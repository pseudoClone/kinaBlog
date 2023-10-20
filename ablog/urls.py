from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('topgauth/', include('django.contrib.auth.urls')), # auth.urls will automatically take care of authentication urls
    path('topgauth/', include('topgauth.urls')), # Like chaining you know
]
