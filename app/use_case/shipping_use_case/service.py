from app.repository.shipping_repository.store import get_shipping, create_shipping, find_all_shippings


def fetch_shipping(shipping_id):
    return get_shipping(shipping_id)


def register_shipping(payload):
    return create_shipping(payload)


def browse_shippings():
    return find_all_shippings()
