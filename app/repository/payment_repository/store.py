from app.constant.payment_constant.values import PAYMENT_PREFIX, PAYMENT_STATUS_DEFAULT
from app.external.payment_external.client import fetch_payment, save_payment, list_payments


def get_payment(payment_id):
    return fetch_payment(payment_id, PAYMENT_STATUS_DEFAULT)


def create_payment(payload):
    payload = payload or {}
    payload.setdefault("prefix", PAYMENT_PREFIX)
    return save_payment(payload)


def find_all_payments():
    return list_payments()
