from fastapi import FastAPI
from router import order

app = FastAPI()
app.include_router(order.router)