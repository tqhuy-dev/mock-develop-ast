from app.constant.product_constant.values import PRODUCT_PREFIX, PRODUCT_STATUS_DEFAULT
from app.external.product_external.client import fetch_product, save_product, list_products


def get_product(product_id):
    return fetch_product(product_id, PRODUCT_STATUS_DEFAULT)


def create_product(payload):
    payload = payload or {}
    payload.setdefault("prefix", PRODUCT_PREFIX)
    return save_product(payload)


def find_all_products():
    return list_products()
