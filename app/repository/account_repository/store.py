from app.constant.account_constant.values import ACCOUNT_PREFIX, ACCOUNT_STATUS_DEFAULT
from app.external.account_external.client import fetch_account, save_account, list_accounts


def get_account(account_id):
    return fetch_account(account_id, ACCOUNT_STATUS_DEFAULT)


def create_account(payload):
    payload = payload or {}
    payload.setdefault("prefix", ACCOUNT_PREFIX)
    return save_account(payload)


def find_all_accounts():
    return list_accounts()
