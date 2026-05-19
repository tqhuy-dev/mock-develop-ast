from app.repository.product_repository.store import get_product, create_product, find_all_products


def fetch_product(product_id):
    return get_product(product_id)


def register_product(payload):
    return create_product(payload)


def browse_products():
    return find_all_products()
