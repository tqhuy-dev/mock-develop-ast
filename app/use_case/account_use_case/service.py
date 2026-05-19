from app.repository.account_repository.store import get_account, create_account, find_all_accounts


def fetch_account(account_id):
    return get_account(account_id)


def register_account(payload):
    return create_account(payload)


def browse_accounts():
    return find_all_accounts()
