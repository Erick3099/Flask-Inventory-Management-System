inventory_data = []
next_id = 1

def reset_inventory():
    global inventory_data, next_id
    inventory_data.clear()
    next_id = 1

def get_all_items():
    return inventory_data

def get_item(item_id):
    return next((item for item in inventory_data if item["id"] == item_id), None)

def add_item(data):
    global next_id

    if "name" not in data or "price" not in data or "stock" not in data:
        raise ValueError("Missing required fields")

    item = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"],
        "brand": data.get("brand"),
        "ingredients": data.get("ingredients")
    }

    inventory_data.append(item)
    next_id += 1
    return item

def update_item(item_id, data):
    item = get_item(item_id)
    if not item:
        return None

    item.update(data)
    return item

def delete_item(item_id):
    global inventory_data
    inventory_data = [item for item in inventory_data if item["id"] != item_id]