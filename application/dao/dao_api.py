from dao.dao_dataclass import PatientData
from dao.dao_prediction_model import DaoPredictionModel
from fastapi import FastAPI
# from model import predict_from_data
# Create FastAPI app
class DaoApi:
    """
    FastAPI application class.
    """
    def __init__(self):
        self._app = FastAPI()
        self._app.post('/predict')(self.fastapi_predict)
        self.model=DaoPredictionModel()

    def app(self):
        return self._app
    
    def fastapi_predict(self, data: PatientData):
        """
        API route to predict based on input data.
        """
        prediction = self.model.predict(data.dict())
        return {'prediction': prediction}
