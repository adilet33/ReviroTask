# FastAPI CRUD App for Products and Establishments
 
This is a sample FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for managing products and establishments.
 
## Features
 
- Create, Read, Update, and Delete products
- Create, Read, Update, and Delete establishments
- Search products and establishments
- API documentation with Swagger UI
 
## Installation
 
1. Install the dependencies:
 
```bash
pip install -r requirements.txt
```
    
 
2. Run the application using Uvicorn:
 
```bash
uvicorn main:app --reload
```
 
3. Alternatively, you can run the application using Docker Compose:
 
```bash
docker-compose -f docker-compose.yaml up -d
```
    
 
## API Documentation
 
Once the application is running, you can access the API documentation at http://localhost:8000/docs.


## Test
```bash
pytest -v
```
