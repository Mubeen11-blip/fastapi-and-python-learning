from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,field_validator,model_validator 
import json

app = FastAPI()
def All_patient_data():
    try:
     with open("patients.json","r") as f:
        return json.load(f)
    except FileNotFoundError:
       raise HTTPException(status_code=500,detail="server configuration erro, this file is not presen")            


# route 1 epi endpint 1
@app.get("/")
def home():
    return {"message":"this is home page"}
# route 2 api end pont 2
@app.get("/about")
def about():
   return {"about us":"this is about us page"}

# route 3
@app.get("/check_patients_data")
def patients():
    data = All_patient_data()
    return data
# route 4
@app.get("/patient_record/{patient_id}")
def individual_pateint_record(patient_id :str):
   data = All_patient_data()
   if patient_id not in data:
        raise HTTPException(status_code=404, detail="this person data is not avalaible")

   return data[patient_id]
