from datetime import datetime
from pydantic import ValidationError
from contract import OrderContract

valid_order = {
    "order_id": "ORD-001",
    "customer_id": 101,
    "amount": 250000.0,
    "status": "PAID",
    "transaction_date": datetime(2026, 9, 20, 8, 0),
    "payment_date": datetime(2026, 9, 20, 8, 15),
}

try:
    order = OrderContract.model_validate(valid_order)

    print("VALID")
    print(order)

except ValidationError as exc:
    print("INVALID")
    print(exc)