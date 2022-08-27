from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mldeploy.urls')),
    path("admin/", admin.site.urls),
]
