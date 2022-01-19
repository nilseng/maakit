from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('maakit/', include('maakit.urls')),
    path('admin/', admin.site.urls),
]
