"""
Run the training model
"""


import joblib

# Get customized functions from ibrary
from preprocess_data import prepare_data, create_train_test_data
from train_model import run_model_training

# 0.Path to data
DATASET_PATH = "../static/dataset/diabetes_dataset.csv"

# 1.Prepare the data
prepared_data = prepare_data(DATASET_PATH)

# 2.Create train - test split
train_test_data = create_train_test_data(
    prepared_data["features"], prepared_data["label"], 0.33, 2023
)

# 3.Run training
model = run_model_training(
    train_test_data["x_train"],
    train_test_data["x_test"],
    train_test_data["y_train"],
    train_test_data["y_test"],
)

# 4.Save the trained model and vectorizer
joblib.dump(model, "../static/model/diabete_detector_model.pkl")
