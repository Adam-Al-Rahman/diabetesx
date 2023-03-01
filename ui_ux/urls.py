"""
UI/UX Interface URL
"""

from django.urls import path
from .views import index

urlpatterns = [
    path("", index),
]
