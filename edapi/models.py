from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Time
from sqlalchemy.types import Date
from database import Base

class donationstable(Base):
	__tablename__ = "Donations"

	did = Column(Integer,primary_key=True,index=True)
	Category = Column(String)
	isDonation = Column(String)
	Description = Column(String)
	donor_address = Column(String,index=True)
	donor_name = Column(String,index=True)
	location = Column(String,index=True)
	postedtime = Column(Time)
	date = Column(Date)
	time = Column(Time)
	quantity = Column(Integer,index=True)
	title = Column(String,index=True)
	user = Column(String)
	image = Column(String)
