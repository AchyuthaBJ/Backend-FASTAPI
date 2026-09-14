from database import Base
from sqlalchemy import Column,String,Float,Integer

class Expense(Base):
    __tablename__ = "Expenses"
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    category = Column(String,nullable=False)
    amount = Column(Float,nullable=False)
    