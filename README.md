# FastAPI Ticket Management API

A simple REST API for managing tickets, built with FastAPI, Pydantic, and SQLAlchemy (SQLite file-based).
## Features
- Create, list, retrieve, update, and close tickets
- Pydantic models for validation
- SQLite file-based DB via SQLAlchemy
- Docker support
- Linting with flake8

## Tech Stack
- Python 3.12+
- FastAPI
- SQLAlchemy
- Pydantic v2
- Pytest
- Flake8
- Docker

## Project Structure
```
fastapi_exp/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routes/
│       └── router.py
├── tests/
│   ├── __init__.py
│   └── test_tickets.py
├── requirements.txt
├── Dockerfile
├── .flake8
├── README.md
```

## Setup
```bash
# Clone the repo
git clone https://github.com/Walidfr/fastapi-ticket-api.git
cd fastapi-ticket-api
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the API
```bash
uvicorn app.main:app --reload
```

## API Docs
Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Run Tests & Coverage
```bash
pytest --cov=app tests/
```

## Lint
```bash
flake8 .
```

## Reset the Database
To delete all data and start fresh, remove the `test.db` file:
```bash
rm test.db
```

## Docker
```bash
docker build -t fastapi-tickets .
docker run -p 8000:8000 fastapi-tickets
```

## Endpoints
- `POST /tickets/` : Create a ticket
- `GET /tickets/` : List all tickets
- `GET /tickets/{ticket_id}` : Get a ticket
- `PUT /tickets/{ticket_id}` : Update a ticket
- `PATCH /tickets/{ticket_id}/close` : Close a ticket

## Example
```bash
curl -X POST "http://localhost:8000/tickets/" -H "Content-Type: application/json" -d '{"title": "Bug", "description": "Something is broken"}'
```
