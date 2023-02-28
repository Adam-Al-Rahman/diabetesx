"""
core URL Configuration

Apps
----
modelapi
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("modelapi.urls")),
    path("", include("ui_ux.urls")),
]
