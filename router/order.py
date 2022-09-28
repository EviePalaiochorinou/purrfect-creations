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

