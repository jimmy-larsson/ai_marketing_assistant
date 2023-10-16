from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketing/', include('marketing.urls')),  # include marketing app urls
]
