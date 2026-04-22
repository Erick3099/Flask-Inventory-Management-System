Flask Inventory Management System

A simple Inventory Management System built with Flask (REST API), a Python CLI client, and pytest tests.
It supports CRUD operations and integration with an external product API (OpenFoodFacts).

   Features
Add, view, update, and delete inventory items
REST API built with Flask
CLI client (Python-based)
External product lookup using barcode API
Automated tests using pytest
In-memory storage (no database required)

Install dependencies
pip install flask requests pytest

     1. Run Flask API Server

Start the backend server first:

python3 app.py

You should see:
Running on http://127.0.0.1:5000

    Run CLI Application

Open a new terminal and run:

python3 cli.py
CLI Menu
Inventory CLI
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

Make sure Flask is running then you open a new terminal you run the python3 cli.py 

python3 app.py
Base URL
http://127.0.0.1:5000
>> Get all items
Method: GET
URL:
http://127.0.0.1:5000/inventory
>>Add item
Method: POST
URL:
http://127.0.0.1:5000/inventory
Body → raw → JSON:
{
  "name": "Milk",
  "price": 4.5,
  "stock": 10
}
>> Get single item
Method: GET
http://127.0.0.1:5000/inventory/1
>> Update item
Method: PATCH
http://127.0.0.1:5000/inventory/1
Body:
{
  "price": 5.5
}
>>Delete item
Method: DELETE
http://127.0.0.1:5000/inventory/1
External API (Barcode Lookup)
Method: GET
http://127.0.0.1:5000/external/<barcode>
Example:
http://127.0.0.1:5000/external/737628064502
Running Tests

Run all tests using:

python3 -m pytest -v

You should see all tests passing.

    Also to note is >>
Data is stored in memory (resets when server restarts)
Flask must be running before using:
CLI
Postman
Default server runs on:
http://127.0.0.1:5000