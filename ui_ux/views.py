"""
Used to implement all the functions that will be triggered when a specific route is called.
In our case, the implementation will be on the prediction function.
"""

# Import necessary libraries
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


# Template WorkLoad
def index(request: HttpRequest) -> HttpResponse:
    """
    From server sending hello.html to client
    Args:
      request: This parameter is passed by the client to this function
    """
    diabetes_status_api_endpoint = ".../api/predict"
    return render(request, "index.html", {"end_point": diabetes_status_api_endpoint})
