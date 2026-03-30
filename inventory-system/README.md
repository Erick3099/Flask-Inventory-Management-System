```bash
pip install -r requirements.txt
 Inventory Management System API
 Overview

This project is a **Flask-based REST API** for managing inventory in a retail environment. It allows users to perform full CRUD (Create, Read, Update, Delete) operations on inventory items and integrates with an external API to fetch real-time product data.

The system also includes a **CLI (Command Line Interface)** for interacting with the API and a **testing suite** to ensure reliability.

Features

Create, read, update, and delete inventory items
Integration with OpenFoodFacts API for product data
CLI interface for user interaction
Unit testing using pytest
In-memory database simulation

---

 Technologies Used

* Python 3
* Flask
* Requests
* Pytest
* Git & GitHub

CLI Usage

Run the CLI:

python cli.py

Features:

View all items
Add item
Update item
Delete item
 Fetch product from external API


how to Run Tests

Run all tests:

pytest -v

Expected result:

13 passed

Error Handling

 Invalid input returns `400 Bad Request`
 Non-existent items return `404 Not Found`
 External API failures handled gracefully



Future Improvements

 Database integration (SQLite/PostgreSQL)
 Authentication & user roles
 Web frontend (React or HTML/CSS)

Author

Developed as part of a Flask REST API lab project.


>License

This project is for educational purposes.
