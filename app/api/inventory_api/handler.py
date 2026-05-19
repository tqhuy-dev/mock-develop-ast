from app.use_case.inventory_use_case.service import fetch_inventory, register_inventory, browse_inventorys


def get_inventory_endpoint(inventory_id):
    return fetch_inventory(inventory_id)


def post_inventory_endpoint(payload):
    return register_inventory(payload)


def list_inventory_endpoint():
    return browse_inventorys()
