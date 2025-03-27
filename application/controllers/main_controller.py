# flask_app.py
import os
import requests
from flask import Flask, render_template, request

class MainController:
    """
    Flask application class.
    """
    def __init__(self,api_url,views_folder_path="../views"):
        """
        Initialize the Flask app and set up routes.
        """
        self._app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), views_folder_path))
        self._api_url=api_url
        self.setup_routes()

    def setup_routes(self):
        """
        Define the routes for the Flask app.
        """
        self._app.add_url_rule('/', 'index', self.index)
        self._app.add_url_rule('/predict', 'flask_predict', self.flask_predict, methods=['POST'])

    def app(self):
        return self._app
    
    def index(self):
        """
        Render the HTML homepage.
        """
        return render_template('index.html')

    def flask_predict(self):
        """
        Handle form submission and send data to FastAPI for prediction.
        """
        data = {
            "Pregnancies": request.form.get('Pregnancies'),
            "PlasmaGlucose": request.form.get('PlasmaGlucose'),
            "DiastolicBloodPressure": request.form.get('DiastolicBloodPressure'),
            "TricepsThickness": request.form.get('TricepsThickness'),
            "SerumInsulin": request.form.get('SerumInsulin'),
            "BMI": request.form.get('BMI'),
            "DiabetesPedigree": request.form.get('DiabetesPedigree'),
            "Age": request.form.get('Age')
        }
        info={
            1:"Living with diabetes is a daily challenge, but every choice you make can make a difference to your health.",
            0:"Preventing diabetes means adopting a healthy lifestyle today to preserve your well-being tomorrow"
        }
        conclusion={
            1:"A person with this characteristic is likely to develop diabetes or will develop it in the future.",
            0:"A person with this characteristic is in good health, i.e. will not develop diabetes."
        }
        # Send data to FastAPI for prediction
        response = requests.post(self._api_url, json=data)
        prediction = response.json()

        return render_template('index.html', prediction=conclusion[prediction['prediction']],diseaseinfo=info[prediction['prediction']])
