# A class wrapper around Airtable API restful sevice

class AirtableApiClient:

    base_url = "https://api.airtable.com/v0/app8wLQrrIMrnn673/Orders"

    # Total orders and number of orders in progress
    def get_orders():
        return {
        "records": [
            {
                "id": "rec9DWw5D4uSUq1zS",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "order_id": 604,
                    "order_placed": "2021-10-05",
                    "product_name": "i heart milk brooch",
                    "price": 68.83,
                    "first_name": "Janeva",
                    "last_name": "Canadine",
                    "address": "2263 Maple Avenue",
                    "email": "jcanadinegr@sphinn.com",
                    "order_status": "in_progress"
                }
            },
            {
                "id": "rec7956R8a1d3gmVC",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "order_id": 726,
                    "order_placed": "2021-10-05",
                    "product_name": "i heart milk brooch",
                    "price": 181.02,
                    "first_name": "Lindsay",
                    "last_name": "Sherrott",
                    "address": "0 Hovde Junction",
                    "email": "lsherrottk5@cornell.edu",
                    "order_status": "placed"
                }
            }
        ]
    }

    # Get the total number of orders this month
    def get_orders_this_month():
        return {
        "records": [
            {
                "id": "rec9DWw5D4uSUq1zS",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "order_id": 604,
                    "order_placed": "2021-10-05",
                    "product_name": "i heart milk brooch",
                    "price": 68.83,
                    "first_name": "Janeva",
                    "last_name": "Canadine",
                    "address": "2263 Maple Avenue",
                    "email": "jcanadinegr@sphinn.com",
                    "order_status": "in_progress"
                }
            },
            {
                "id": "rec7956R8a1d3gmVC",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "order_id": 726,
                    "order_placed": "2021-10-05",
                    "product_name": "i heart milk brooch",
                    "price": 181.02,
                    "first_name": "Lindsay",
                    "last_name": "Sherrott",
                    "address": "0 Hovde Junction",
                    "email": "lsherrottk5@cornell.edu",
                    "order_status": "placed"
                }
            }
        ]
    }

    # Revenue after removing cancelled orders, keeps only price and order status fields
    def get_revenue():
        return {
        "records": [
            {
                "id": "rec9DWw5D4uSUq1zS",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "price": 68.83,
                    "order_status": "in_progress"
                }
            },
            {
                "id": "rec7956R8a1d3gmVC",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "price": 181.02,
                    "order_status": "placed"
                }
            }
        ]
    }

    # A list of the most recent few orders (use of sort and pageSize)
    def get_the_10_most_recent_orders():
        return {
        "records": [
            {
                "id": "rec9DWw5D4uSUq1zS",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "order_id": 604,
                    "order_placed": "2021-10-05",
                    "product_name": "i heart milk brooch",
                    "price": 68.83,
                    "first_name": "Janeva",
                    "last_name": "Canadine",
                    "address": "2263 Maple Avenue",
                    "email": "jcanadinegr@sphinn.com",
                    "order_status": "in_progress"
                }
            },
            {
                "id": "rec7956R8a1d3gmVC",
                "createdTime": "2021-10-06T09:16:38.000Z",
                "fields": {
                    "order_id": 726,
                    "order_placed": "2021-10-05",
                    "product_name": "i heart milk brooch",
                    "price": 181.02,
                    "first_name": "Lindsay",
                    "last_name": "Sherrott",
                    "address": "0 Hovde Junction",
                    "email": "lsherrottk5@cornell.edu",
                    "order_status": "placed"
                }
            }
        ]
    }