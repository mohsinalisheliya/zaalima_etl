from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payments'
    
    # Notice how we are using 'comment=' here!
    id = Column(Integer, primary_key=True, comment="Unique transaction ID")
    amount = Column(Float, nullable=False, comment="Payment amount must be positive")
    status = Column(String, nullable=False)
    currency = Column(String, default="USD")