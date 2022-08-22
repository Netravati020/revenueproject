from fastapi import FastAPI, Depends
from sqlalchemy import select

from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models


app=FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)

@app. post('/')
def read_adm(db: Session=Depends(get_db)):

    result = db.query(models.Admission).join(models.Patient_data, models.Admission.branch == models.Patient_data.branch_id).all()
    print("branch: {} plan: {}".format(models.Admission.branch, models.Admission.plan))





