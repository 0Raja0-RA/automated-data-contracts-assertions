from datetime import datetime
from pydantic import ValidationError
from contract import OrderContract

invalid_order = {
    "order_id": "ORD-999",
    "customer_id": 999,
    "amount": 100000.0,
    "status": "PAID",
    "transaction_date": datetime(2026, 9, 20, 10, 0),
    "payment_date": None,
}

try:
    order = OrderContract.model_validate(invalid_order)

    print("VALID")

except ValidationError as exc:
    print("INVALID")
    print(exc)