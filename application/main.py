# app.py
import threading
from controllers.main_controller import MainController
from dao.dao_api import DaoApi
import uvicorn
# from flask_app import app as flask_app
# from fastapi_app import app as fastapi_app

def run_fastapi():
    """Run FastAPI app."""
    fastapi_app=DaoApi()
    uvicorn.run(fastapi_app.app(), host="0.0.0.0", port=8000)

if __name__ == "__main__":
    FASTAPI_URL = "http://0.0.0.0:8000/predict"   
    flask_app=MainController(FASTAPI_URL)
    # Start FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()
    # Start Flask app
    flask_app.app().run(host='0.0.0.0', port=5000,debug=True, use_reloader=False)
