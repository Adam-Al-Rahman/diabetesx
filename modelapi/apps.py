"""
App modelapi
"""

import os
import joblib

from django.apps import AppConfig
from django.conf import settings


class ModelApiConfig(AppConfig):
    """
    Load machine learning models in apps.py so that when the application starts,\n
    the trained model is loaded only once. Otherwise, the trained model is loaded each\n
    time an endpoint is called, and then the response time will be slower.
    """

    name = "modelapi"

    # Load the model from the static folder
    MODEL_PATH = os.path.join(settings.BASE_DIR, "static/model/")
    model = joblib.load(open(MODEL_PATH + "diabete_detector_model.pkl", "rb"))
