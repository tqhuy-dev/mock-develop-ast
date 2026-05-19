from app.use_case.account_use_case.service import fetch_account, register_account, browse_accounts


def get_account_endpoint(account_id):
    return fetch_account(account_id)


def post_account_endpoint(payload):
    return register_account(payload)


def list_account_endpoint():
    return browse_accounts()
