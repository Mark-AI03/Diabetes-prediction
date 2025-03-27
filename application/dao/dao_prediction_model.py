import os
import joblib
import pandas as pd

class DaoPredictionModel:
    """
    Class for loading the trained model and making predictions.
    """

    def __init__(self, model_path="../models/grandiantBoostingClassifier.pkl"):
        """
        Load the model from the given file path.
        """
        self.model = joblib.load(self.__manage_path__(model_path))

    def __manage_path__(self, model_path):

        script_dir = os.path.dirname(os.path.abspath(__file__))# find current dir
        model_path = os.path.join(script_dir, model_path)
        return model_path
    def predict(self, data):
        """
        Predict the result based on the provided data.
        """
        df = pd.DataFrame([data])
        prediction = self.model.predict(df)
        return int(prediction[0])
