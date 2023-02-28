"""
Training model
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def run_model_training(x_train, x_test, y_train, y_test):
    """
    Train model
    """
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    clf.score(x_test, y_test)
    y_pred = clf.predict(x_test)
    print("\n3. Model Performance: \n")
    print(classification_report(y_test, y_pred))

    return clf
