from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String
Base = declarative_base()

class PaymentRecord(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    status = Column(String, nullable=False)

class SalesforceLead(Base):
    __tablename__ = "salesforce_leads"

    lead_id = Column(String, primary_key=True, comment="SFDC Unique ID")
    company = Column(String, nullable=False)
    status = Column(String, nullable=False)
    
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    status = Column(String)