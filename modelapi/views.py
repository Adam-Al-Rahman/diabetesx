"""
Used to implement all the functions that will be triggered when a specific route is called.
In our case, the implementation will be on the prediction function.
"""

# Import necessary libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response

import numpy as np

from .apps import ModelApiConfig


@api_view(["POST"])
def predict_patient_status(request):
    """
    Predict patient status\n
    Request Method: Post
    """
    try:
        # load the request data
        patient_json_info = request.data

        # Retrieve all the values from the json data
        patient_info = np.array(list(patient_json_info.values()))

        # Make prediction
        patient_status = ModelApiConfig.model.predict([patient_info])

        # Model confidence score
        model_confidence_score = np.max(
            ModelApiConfig.model.predict_proba([patient_info])
        )

        model_prediction = {
            "info": "success",
            "patient_status": patient_status[0],
            "model_confidence_proba": float(f"{(model_confidence_score * 100):.2f}"),
        }

    except ValueError as v_err:
        model_prediction = {"error_code": "-1", "info": str(v_err)}

    return Response(model_prediction, status=200)
