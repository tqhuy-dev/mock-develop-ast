from app.use_case.catalog_use_case.service import fetch_catalog, register_catalog, browse_catalogs


def get_catalog_endpoint(catalog_id):
    return fetch_catalog(catalog_id)


def post_catalog_endpoint(payload):
    return register_catalog(payload)


def list_catalog_endpoint():
    return browse_catalogs()
