from app.constant.inventory_constant.values import INVENTORY_PREFIX, INVENTORY_STATUS_DEFAULT
from app.external.inventory_external.client import fetch_inventory, save_inventory, list_inventorys


def get_inventory(inventory_id):
    return fetch_inventory(inventory_id, INVENTORY_STATUS_DEFAULT)


def create_inventory(payload):
    payload = payload or {}
    payload.setdefault("prefix", INVENTORY_PREFIX)
    return save_inventory(payload)


def find_all_inventorys():
    return list_inventorys()
