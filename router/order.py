from fastapi import APIRouter
from client import airtable_api_client
from datetime import datetime

router = APIRouter(
    prefix='/dashboard',
    tags=['dashboard']
)

@router.get('/')
def get_aggregate_data():
    client = airtable_api_client.AirtableApiClient
    orders = client.get_orders()
    aggregate_data = {
        "number of orders": _get_orders(orders),
        "number of orders this month": _get_total_orders_this_month(orders),
        "number of orders in progress": _get_orders_in_progress(orders),
        "revenue": _get_revenue(orders),
        "most recent orders": _get_recent_orders(orders),
        "placed orders": _get_placed_orders(orders)
    }
    return aggregate_data

def _get_orders(orders):
    return len(orders)

def _get_total_orders_this_month(orders):
    today = datetime.now()
    orders_this_month = []
    for order in orders:
        fields = order["fields"]
        order_date = datetime.fromisoformat(fields["order_placed"])
        if today.year == order_date.year and today.month == order_date.month:
            orders_this_month.append(order)
    return orders_this_month

def _get_orders_in_progress(orders):
    orders_in_progress = []
    for order in orders:
        fields = order["fields"]
        if fields["order_status"] == "in_progress":
            orders_in_progress.append(order)
    return len(orders)

def _get_revenue(orders):
    # Valid orders are all orders minus the cancelled ones
    revenue = 0
    for order in orders:
        fields = order["fields"]
        if fields["order_status"] != "cancelled":
            revenue += fields["price"]
    return revenue

def _get_recent_orders(orders):
    recent_orders = orders[:10]
    return recent_orders

def _get_placed_orders(orders):
    placed_orders = []
    for order in orders:
        fields = order["fields"]
        if fields["order_status"] == "placed":
            placed_orders.append(order)
    return placed_orders