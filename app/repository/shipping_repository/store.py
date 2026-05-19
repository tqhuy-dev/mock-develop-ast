from app.constant.shipping_constant.values import SHIPPING_PREFIX, SHIPPING_STATUS_DEFAULT
from app.external.shipping_external.client import fetch_shipping, save_shipping, list_shippings


def get_shipping(shipping_id):
    return fetch_shipping(shipping_id, SHIPPING_STATUS_DEFAULT)


def create_shipping(payload):
    payload = payload or {}
    payload.setdefault("prefix", SHIPPING_PREFIX)
    return save_shipping(payload)


def find_all_shippings():
    return list_shippings()
