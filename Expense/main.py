from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import engine,get_db
app = FastAPI()

class Expense(BaseModel):
    amount:float
    category:str
    
models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session,Depends(get_db)]
@app.get("/expenses")
async def get_all_expenses(db:db_dependency):
    try:
        expenses = db.query(models.Expense).all()
        return expenses
    except Exception as e:
        raise e

@app.get("/expenses/")
async def get_all_expenses(db:db_dependency,category:str):
    try:
        results = db.query(models.Expense).filter(models.Expense.category == category).all()
        return results
    except Exception as e:
        raise e

@app.get("/expenses/summary")
async def get_expense_summary(db:db_dependency):
    try:
        from sqlalchemy import func
        result = (
            db.query(
                models.Expense.category,
                func.sum(models.Expense.amount).label("total")
            )
            .group_by(models.Expense.category)
            .all()
        )
        return [
    {
        "category": category,
        "total": total
    }
    for category, total in result
]
    except Exception as e:
        raise e

@app.post("/expenses")
async def create_expense(db:db_dependency,expense:Expense):
    try:
        new_expense = models.Expense(**expense.model_dump())
        db.add(new_expense)
        db.commit()
    except Exception as e:
        raise e
    return expense.model_dump()

@app.delete("/expenses/{id}")
async def delete_expense(id:int,db:db_dependency):
    try:
        db.query(models.Expense).filter(models.Expense.id == id).delete()
        db.commit()
    except Exception as e:
        raise e
    return {"id":id}

@app.put("/expenses/{id}")
async def update_expense(id:int,db:db_dependency,expense:Expense):
    try:
        db_expense = db.query(models.Expense).filter(models.Expense.id == id).first()
        db_expense.amount = expense.amount
        db_expense.category = expense.category
        db.commit()
        return db_expense
    except Exception as e:
        raise e

@app.get("/expenses/{id}")
async def get_expense(id:int,db:db_dependency):
    try:
        expense = db.query(models.Expense).filter(models.Expense.id == id).first()
        return expense
    except Exception as e:
        raise e






