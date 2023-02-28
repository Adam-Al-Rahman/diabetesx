"""
UI/UX Interface URL
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
]
