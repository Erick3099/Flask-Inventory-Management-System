# Flask Inventory Management System

A simple Inventory Management System built with **Flask REST API**, a **Python CLI client**, and **pytest tests**.  
It supports full CRUD operations and integrates with an external product API (OpenFoodFacts).

## Features

Add, view, update, and delete inventory items (CRUD)
REST API built with Flask
Python CLI client for interacting with the API
External product lookup using barcode (OpenFoodFacts API)
Automated tests using pytest
In-memory storage (no database required)

## Tech Stack

- Python 3.10+
- Flask
- Requests
- Pytest
- Pipenv (recommended)

## Project Structure
inventory-system/
-- app.py # Flask API server
--cli.py # CLI application
--inventory.py # Inventory CRUD logic
--external_api.py # External API integration
--tests/ # Pytest test cases
--Pipfile # Dependencies
--Pipfile.lock # Locked dependencies

## Setup Instructions

### 1. Clone the repository
git clone <your-repo-url>
cd Flask-Inventory-Management-System/inventory-system

2. Install Pipenv  
## pip install pipenv

3. Install dependencies
## pipenv install flask requests pytest

4. Activate virtual environment
## pipenv shell

>>Running the Application
Start Flask API server by using 
## python app.py  where server runs at : http://127.0.0.1:5000

>>Run CLI (new terminal)
pipenv shell
python cli.py

## python cli.py CLI Menu Inventory CLI 
1.View all items 
2.Add item 
3.Update item 
4.Delete item 
5.Fetch from API 
6.Exit 
Example (Add item) 
Choose option: 2 
Name: Milk 
Price: 4.5 
Stock: 10 
Using Postman (API Testing) 
## Make sure Flask is running then you open a new terminal you run the python3 cli.py

 ## python app.py
API Endpoints
Method	Endpoint	Description
GET	/	API health check
GET	/inventory	Get all items
GET	/inventory/<id>	Get single item
POST	/inventory	Add new item
PATCH	/inventory/<id>	Update item
DELETE	/inventory/<id>	Delete item
GET	/external/<barcode>	Fetch product details

### Example Request
Add Item (POST)
{
  "name": "eggs",
  "price": 4.5,
  "stock": 12
}

## Running Tests
pytest -v or use python -m pytest -v

## you should see all tests passing 

## Always Note that !
Data is stored in memory (resets when server restarts)
Flask server must be running before using CLI or API tools
Always run commands inside pipenv shell

## Common Issues
Connection refused

Start the Flask server first:

>> python app.py
Module not found

## Reinstall dependencies:

>>pipenv install
>>pipenv shell

## Author

Erick Wambua

