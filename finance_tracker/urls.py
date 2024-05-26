# finance_tracker/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Homepage
    path('users/', include('users.urls')),
    path('finance/', include('finance.urls')),
    path('notifications/', include('notifications.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
