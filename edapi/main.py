from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import Null
import models, schema
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from database import SessionLocal, engine
import uvicorn

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return {"message" : "Server is Running!!"}

@app.get("/donations/", response_model=List[schema.Donationsschema])
def get_donations(db : Session = Depends(get_db)):
    return db.query(models.donationstable).all()    

@app.get("/donations/{id}", response_model = schema.Donationsschema)
def get_donations_by_id(id : int, db : Session = Depends(get_db)):
    x = db.query(models.donationstable).filter(models.donationstable.did == id).first()
    if x:
        return x
    else:
    	raise HTTPException(status_code=404, detail = "User not found")

@app.post("/donations/add/", response_model = schema.Donationsschema)
def create_donation(context : schema.Donationsschema, db : Session = Depends(get_db)):
    x = db.query(models.donationstable).filter(models.donationstable.did == context.id).first()
    if x:
        raise HTTPException(status_code = 400 ,detail = "Donations Already Exists!!") 
    db_donations = models.donationstable(
		did = donationstable.did,
		Category = donationstable.Category,
		isDonation = donationstable.isDonation,
		Description = donationstable.Description,
		donor_address = donationstable.donor_address,
		donor_name = donationstable.donor_name,
		location = donationstable.location,
		postedtime = donationstable.postedtime,
		date = donationstable.date,
		time = donationstable.time,
		quantity = donationstable.quantity,
		title = donationstable.title,
		user = donationstable.user,
		image = donationstable.image,
    )
    db.add(db_donations)
    db.commit()
    db.refresh(db_donations)
    return db_donations    