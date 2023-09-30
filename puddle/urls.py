from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index,contact

urlpatterns = [
    path('', index, name = 'index'),
    path('items', include('item.urls')), # Go to the items urls and find urls var in there
    path('contact/', contact, name = 'contact'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
