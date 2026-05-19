from app.constant.catalog_constant.values import CATALOG_PREFIX, CATALOG_STATUS_DEFAULT
from app.external.catalog_external.client import fetch_catalog, save_catalog, list_catalogs


def get_catalog(catalog_id):
    return fetch_catalog(catalog_id, CATALOG_STATUS_DEFAULT)


def create_catalog(payload):
    payload = payload or {}
    payload.setdefault("prefix", CATALOG_PREFIX)
    return save_catalog(payload)


def find_all_catalogs():
    return list_catalogs()
