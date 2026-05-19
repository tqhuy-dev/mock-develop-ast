from app.repository.payment_repository.store import get_payment, create_payment, find_all_payments


def fetch_payment(payment_id):
    return get_payment(payment_id)


def register_payment(payload):
    return create_payment(payload)


def browse_payments():
    return find_all_payments()
