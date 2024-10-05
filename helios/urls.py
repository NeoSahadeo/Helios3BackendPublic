from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/auth/', include('knox.urls')),
    path('', include('app.urls')),
]
