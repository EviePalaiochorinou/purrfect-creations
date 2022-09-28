from fastapi import APIRouter
from client import airtable_api_client

router = APIRouter(
    prefix='/order',
    tags=['order']
)

@router.get('/')#, response_model = OrderDisplay)
def get_orders():
    return airtable_api_client.get_orders()