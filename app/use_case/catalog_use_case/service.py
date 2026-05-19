from app.repository.catalog_repository.store import get_catalog, create_catalog, find_all_catalogs


def fetch_catalog(catalog_id):
    return get_catalog(catalog_id)


def register_catalog(payload):
    return create_catalog(payload)


def browse_catalogs():
    return find_all_catalogs()
