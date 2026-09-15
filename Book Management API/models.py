from database import Base
from sqlalchemy import Column, Integer, String, Boolean,Float


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    year = Column(Integer)
    availability = Column(Boolean,default=True)