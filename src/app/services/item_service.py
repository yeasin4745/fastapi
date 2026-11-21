from app.schemas.item import ItemCreate, ItemUpdate


# Temporary in-memory storage
items = {}

next_id = 1


# CREATE
def create_item(item: ItemCreate):

    global next_id

    new_item = {
        "id": next_id,
        **item.model_dump()
    }

    items[next_id] = new_item

    next_id += 1

    return new_item


# READ ALL
def get_all_items():

    return list(items.values())


# READ ONE
def get_item(item_id: int):

    return items.get(item_id)


# UPDATE
def update_item(item_id: int, item: ItemUpdate):

    if item_id not in items:
        return None

    updated_item = {
        "id": item_id,
        **item.model_dump()
    }

    items[item_id] = updated_item

    return updated_item


# DELETE
def delete_item(item_id: int):

    if item_id not in items:
        return False

    del items[item_id]

    return True
