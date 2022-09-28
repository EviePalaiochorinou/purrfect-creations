from fastapi import APIRouter
from client import airtable_api_client
from datetime import datetime

router = APIRouter(
    prefix='/dashboard',
    tags=['dashboard']
)

@router.get('/orders')#, response_model = OrderDisplay)
def get_orders():
    orders = airtable_api_client.get_orders()
    return len(orders)

@router.get('/orders-current-month')
def get_total_orders_this_month():
    today = datetime.now()
    orders = airtable_api_client.get_orders()
    orders_this_month = []
    for order in orders:
        fields = order["fields"]
        order_date = datetime.fromisoformat(fields["order_placed"])
        if today.year == order_date.year and today.month == order_date.month:
            orders_this_month.append(order)
    return orders_this_month

@router.get('/orders-in-progress')
def get_orders_in_progress():
    orders = airtable_api_client.get_orders()
    orders_in_progress = []
    for order in orders:
        fields = order["fields"]
        if fields["order_status"] == "in_progress":
            orders_in_progress.append(order)
    return len(orders)

@router.get('/revenue')
def get_revenue():
    orders = airtable_api_client.get_orders()
    # Valid orders are all orders minus the cancelled ones
    revenue = 0
    for order in orders:
        fields = order["fields"]
        if fields["order_status"] != "cancelled":
            revenue += fields["price"]
    
    return revenue
