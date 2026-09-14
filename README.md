# Expense Tracker API

A simple REST API for managing expenses, built as a learning project using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## 🚀 Features

- Create expenses
- Retrieve all expenses
- Retrieve an expense by ID
- Update expenses
- Delete expenses
- Get total expenses grouped by category
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request validation
- FastAPI dependency injection
- Automatic interactive API documentation

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Psycopg2
- Uvicorn

## 📁 Project Structure

```text
expense-tracker/
│
├── main.py          # FastAPI application and API endpoints
├── database.py      # Database connection and session management
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic schemas for validation
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## 🗄️ Architecture

The project separates the database and API responsibilities into different files:

```text
                    FastAPI
                       │
                       ▼
                    main.py
                       │
              ┌────────┴────────┐
              ▼                 ▼
         schemas.py         models.py
              │                 │
              │                 ▼
              │            database.py
              │                 │
              └────────┬────────┘
                       ▼
                   PostgreSQL
```

### `database.py`

Responsible for:

- Creating the SQLAlchemy engine
- Creating database sessions
- Defining the SQLAlchemy `Base`
- Providing the database dependency with `get_db()`

### `models.py`

Contains SQLAlchemy models that represent database tables.

Example:

```python
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    category = Column(String)
```

### `schemas.py`

Contains Pydantic models used to validate data received by the API.

### `main.py`

Contains the FastAPI application and API endpoints.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd expense-tracker
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE fastapi;
```

Then configure the SQLAlchemy database URL.

Example:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/fastapi"
```

> **Security:** Do not commit real database passwords or other secrets to GitHub. Use environment variables for production projects.

## ▶️ Run the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/expenses` | Get all expenses |
| GET | `/expenses/{expense_id}` | Get an expense by ID |
| POST | `/expenses` | Create a new expense |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |
| GET | `/expenses/summary` | Get total expenses by category |

> **Note:** Define `/expenses/summary` before `/expenses/{expense_id}` so that `summary` is not interpreted as an `expense_id`.

## 📝 Example Request

### Create an Expense

```http
POST /expenses
```

Request body:

```json
{
  "amount": 250.50,
  "category": "Food"
}
```

Example response:

```json
{
  "id": 1,
  "amount": 250.50,
  "category": "Food"
}
```

## 📊 Expense Summary

The summary endpoint groups expenses by category and calculates the total amount spent.

```http
GET /expenses/summary
```

Example response:

```json
[
  {
    "category": "Food",
    "total": 400.50
  },
  {
    "category": "Shopping",
    "total": 1950.00
  },
  {
    "category": "Transport",
    "total": 430.00
  }
]
```

The SQLAlchemy query is equivalent to:

```sql
SELECT category, SUM(amount) AS total
FROM expenses
GROUP BY category;
```

## 🧠 Concepts Practiced

This project was created to practice the fundamentals of backend development with FastAPI:

- REST API design
- CRUD operations
- HTTP methods
- HTTP status codes
- FastAPI dependency injection
- Pydantic models
- SQLAlchemy ORM
- PostgreSQL
- Database sessions
- SQL aggregation
- `SUM()` and `GROUP BY`
- API request validation
- Automatic API documentation

## 🔮 Future Improvements

Some possible improvements for future versions:

- JWT authentication
- User accounts
- User-specific expenses
- Expense dates
- Filtering and pagination
- Search expenses by category
- Monthly expense reports
- Budget tracking
- Alembic database migrations
- Automated tests with Pytest
- Docker support
- Frontend integration

## 👨‍💻 Author

**Achyutha B Jagadeesh**

This project was built as a learning project to gain practical experience with **Python backend development, FastAPI, SQLAlchemy, and PostgreSQL**.
