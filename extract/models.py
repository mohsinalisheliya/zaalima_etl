from pydantic import BaseModel, Field
from typing import Optional

class PaymentRecord(BaseModel):
    id: int = Field(..., description="Unique transaction ID")
    amount: float = Field(..., gt=0, description="Payment amount must be positive")
    status: str
    currency: Optional[str] = "USD"