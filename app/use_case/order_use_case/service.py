from app.repository.order_repository.store import get_order, create_order, find_all_orders
from app.use_case.order_use_case.validator import validate_order_product


def fetch_order(order_id):
    validate_order_product()
    return get_order(order_id)


def register_order(payload):
    return create_order(payload)


def browse_orders():
    return find_all_orders()
