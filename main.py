"""Entry point: invoke API handlers across domains."""

from app.api.order_api.handler import get_order_endpoint, list_order_endpoint
from app.api.product_api.handler import get_product_endpoint
from app.api.account_api.handler import get_account_endpoint
from app.api.inventory_api.handler import list_inventory_endpoint
from app.api.payment_api.handler import post_payment_endpoint
from app.api.shipping_api.handler import get_shipping_endpoint
from app.api.catalog_api.handler import list_catalog_endpoint


def run_demo():
    get_order_endpoint("ord-1")
    list_order_endpoint()
    get_product_endpoint("prd-1")
    get_account_endpoint("acc-1")
    list_inventory_endpoint()
    post_payment_endpoint({"amount": 0})
    get_shipping_endpoint("shp-1")
    list_catalog_endpoint()
    print("demo completed")


if __name__ == "__main__":
    run_demo()
