from app.use_case.order_use_case.service import fetch_order, register_order, browse_orders


def get_order_endpoint(order_id):
    return fetch_order(order_id)


def post_order_endpoint(payload):
    return register_order(payload)


def list_order_endpoint():
    return browse_orders()
