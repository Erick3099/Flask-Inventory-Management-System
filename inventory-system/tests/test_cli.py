import pytest
from inventory import reset_inventory, add_item, get_all_items

def test_cli_add_item():
    reset_inventory() 
    add_item({"name": "Juice", "price": 3, "stock": 10})
    items = get_all_items()
    assert len(items) == 1
    assert items[0]["name"] == "Juice"

def test_cli_multiple_items():
    reset_inventory() 
    add_item({"name": "Soda", "price": 1.5, "stock": 20})
    add_item({"name": "Water", "price": 1, "stock": 15})
    items = get_all_items()
    assert len(items) == 2