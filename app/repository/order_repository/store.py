from app.constant.order_constant.values import ORDER_PREFIX, ORDER_STATUS_DEFAULT
from app.external.order_external.client import fetch_order, save_order, list_orders


def get_order(order_id):
    return fetch_order(order_id, ORDER_STATUS_DEFAULT)


def create_order(payload):
    payload = payload or {}
    payload.setdefault("prefix", ORDER_PREFIX)
    return save_order(payload)


def find_all_orders():
    return list_orders()
