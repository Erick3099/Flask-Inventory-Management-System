import pytest
from app import app
from inventory import reset_inventory

@pytest.fixture
def client():
    reset_inventory()  
    return app.test_client()

def test_get_empty_inventory(client):
    rv = client.get("/inventory")
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_post_item(client):
    rv = client.post("/inventory", json={
        "name": "Milk",
        "price": 2.5,
        "stock": 10
    })
    data = rv.get_json()
    assert rv.status_code == 201
    assert data["id"] == 1   
    assert data["name"] == "Milk"

def test_get_single_item(client):
    client.post("/inventory", json={"name":"Bread","price":3,"stock":5})
    rv = client.get("/inventory/1")
    assert rv.status_code == 200

def test_patch_item(client):
    client.post("/inventory", json={"name":"Eggs","price":5,"stock":12})
    rv = client.patch("/inventory/1", json={"price":6})
    assert rv.status_code == 200

def test_delete_item(client):
    client.post("/inventory", json={"name":"Cheese","price":4,"stock":8})
    rv = client.delete("/inventory/1")
    assert rv.status_code == 200

def test_get_invalid_item(client):
    rv = client.get("/inventory/999")
    assert rv.status_code == 404

def test_patch_invalid_item(client):
    rv = client.patch("/inventory/999", json={"price":10})
    assert rv.status_code == 404

def test_delete_invalid_item(client):
    rv = client.delete("/inventory/999")
    assert rv.status_code == 404

def test_post_invalid_data(client):
    rv = client.post("/inventory", json={"foo": "bar"})
    assert rv.status_code == 400