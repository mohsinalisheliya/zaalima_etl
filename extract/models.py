from pydantic import BaseModel, EmailStr
from typing import Optional

class Payment(BaseModel):
    id: str
    amount: float
    currency: str
    status: str
    created: str
    customer_email: Optional[str] = None

class Customer(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    created: str