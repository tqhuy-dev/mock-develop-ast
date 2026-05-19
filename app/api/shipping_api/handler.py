from app.use_case.shipping_use_case.service import fetch_shipping, register_shipping, browse_shippings


def get_shipping_endpoint(shipping_id):
    return fetch_shipping(shipping_id)


def post_shipping_endpoint(payload):
    return register_shipping(payload)


def list_shipping_endpoint():
    return browse_shippings()
