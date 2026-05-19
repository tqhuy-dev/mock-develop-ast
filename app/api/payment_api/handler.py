from app.use_case.payment_use_case.service import fetch_payment, register_payment, browse_payments


def get_payment_endpoint(payment_id):
    return fetch_payment(payment_id)


def post_payment_endpoint(payload):
    return register_payment(payload)


def list_payment_endpoint():
    return browse_payments()
