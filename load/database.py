
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


load_dotenv()

from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file.")


engine = create_engine(
    DATABASE_URL,
    pool_size=20,          
    max_overflow=10,       
    pool_timeout=30,       
    pool_pre_ping=True,    
    future=True
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(" Connected to the database successfully!")
    except Exception as e:
        print(" Connection failed")
        print(e)