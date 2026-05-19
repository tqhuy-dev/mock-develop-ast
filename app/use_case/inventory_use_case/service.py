from app.repository.inventory_repository.store import get_inventory, create_inventory, find_all_inventorys


def fetch_inventory(inventory_id):
    return get_inventory(inventory_id)


def register_inventory(payload):
    return create_inventory(payload)


def browse_inventorys():
    return find_all_inventorys()
