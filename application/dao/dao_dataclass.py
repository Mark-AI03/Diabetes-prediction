from pydantic import BaseModel
class PatientData(BaseModel):
    Pregnancies: int
    PlasmaGlucose: float
    DiastolicBloodPressure: float
    TricepsThickness: float
    SerumInsulin: float
    BMI: float
    DiabetesPedigree: float
    Age: int