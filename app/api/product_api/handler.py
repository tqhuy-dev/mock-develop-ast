from app.use_case.product_use_case.service import fetch_product, register_product, browse_products


def get_product_endpoint(product_id):
    return fetch_product(product_id)


def post_product_endpoint(payload):
    return register_product(payload)


def list_product_endpoint():
    return browse_products()
