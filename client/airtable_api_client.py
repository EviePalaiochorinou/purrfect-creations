from pyairtable import Table
import os
# A class wrapper around Airtable API restful sevice
class AirtableApiClient:

    def __init__(self) -> None:
        airtable_key = os.environ["AIRTABLE_KEY"]
        self.airtable_orders_client = Table(airtable_key, "app8wLQrrIMrnn673","tblZBNaHCGVfA9xw1")

    # I have limited the number of the results coming back, for ease of development and a faster response
    def get_orders(self):
        orders = self.airtable_orders_client.all(sort=["-order_placed"], max_records = 50)
        return orders
