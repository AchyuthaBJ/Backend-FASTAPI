from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import func
from sqlalchemy.sql.operators import and_

from models import Book
import models
from pydantic import BaseModel, Field
from database import get_db,engine
from typing import Annotated
from sqlalchemy.orm import Session


db_dependency = Annotated[Session,Depends(get_db)]

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class BookBase(BaseModel):
    name : str = Field(min_length=5)
    price :float = Field(gt=10)
    category : str = Field(min_length=5)
    year : int = Field(gt=1980, lt=2030)
    availability :bool = Field(default=True)

@app.get("/book")
async def get_books(db:db_dependency, mini:int, maxi:int):
    books = db.query(Book).filter(and_(Book.price > mini, Book.price < maxi)).all()
    if books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books


@app.get("/books")
async def get_all_books(db:db_dependency):
    res = db.query(Book).all()
    return res

@app.get("/books/statistics")
async def get_book_statistics(db:db_dependency):
    total_books = db.query(Book).count()
    avail_books = db.query(Book).filter(Book.availability.is_(True)).count()
    not_avail_books = db.query(Book).filter(Book.availability.is_(False)).count()
    avg_price = db.query(func.avg(Book.price)).scalar()

    return {
        "total_books":total_books,
        "avail_books":avail_books,
        "not_avail_books":not_avail_books,
        "avg_price":avg_price,
    }


@app.get("/books/{id}")
async def get_book(id:int,db:db_dependency):
    res = db.query(Book).filter(Book.id == id).first()
    if res is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return res
@app.post("/books")
async def create_book(book:BookBase,db:db_dependency):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    return new_book

@app.put("/books/{id}")
async def update_book(id:int,book:BookBase,db:db_dependency):
    update_book = db.query(Book).filter(Book.id == id).first()
    if update_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    update_book.name = book.name
    update_book.price = book.price
    update_book.category = book.category
    update_book.year = book.year
    update_book.availability = book.availability
    db.commit()
    return update_book

@app.delete("/books/{id}")
async def delete_book(id:int,db:db_dependency):
    delete_book = db.query(Book).filter(Book.id == id).first()
    if delete_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(delete_book)
    db.commit()
    return delete_book

@app.get("/books/category/{category}")
async def get_book_category(category: str,db:db_dependency):
    category_book = db.query(Book).filter(Book.category == category).all()
    if category_book is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category_book

@app.get("/books/availability/")
async def get_book_availability(db:db_dependency):
    availability_book = db.query(Book).filter(Book.availability == True).all()
    if availability_book is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return availability_book



