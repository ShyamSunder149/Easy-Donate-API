from datetime import date,time
from pydantic import BaseModel


class Donationsschema(BaseModel):
    did : int
    Category : str
    isDonation : str
    Description : str
    donor_address : str
    donor_name : str
    location : str
    postedtime : time
    date : date
    time : time
    quantity : int
    title : str
    user : str
    image : str
    class Config:
        orm_mode = True