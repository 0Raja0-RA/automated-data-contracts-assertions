import csv
from datetime import datetime
from pydantic import ValidationError
from contract import OrderContract

def parse_datetime(value):
    if value is None or value == "":
        return None
    return datetime.fromisoformat(value)

def load_orders(path):
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(
                {
                    "order_id": row["order_id"],
                    "customer_id": int(row["customer_id"]),
                    "amount": float(row["amount"]),
                    "status": row["status"],
                    "transaction_date": parse_datetime(
                        row["transaction_date"]
                    ),
                    "payment_date": parse_datetime(
                        row["payment_date"]
                    ),
                }
            )
        return rows

def validate_batch(rows):
    errors = []
    valid_orders = []
    for row_number, row in enumerate(rows, start=2):
        try:
            order = OrderContract.model_validate(row)
            valid_orders.append(order)
        except ValidationError as exc:
            errors.append(
                {
                    "row": row_number,
                    "order_id": row.get("order_id"),
                    "errors": exc.errors(),
                }
            )
    return valid_orders, errors

rows = load_orders("../data/orders_valid.csv")
valid_orders, errors = validate_batch(rows)

print(f"Jumlah record : {len(rows)}")
print(f"Valid         : {len(valid_orders)}")
print(f"Invalid       : {len(errors)}")