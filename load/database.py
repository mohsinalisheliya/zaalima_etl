import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# Get the database URL from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file.")

# Create SQLAlchemy engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=20,          # Maximum number of permanent connections
    max_overflow=10,       # Allow 10 extra temporary connections
    pool_timeout=30,       # Wait 30 seconds before timing out
    pool_pre_ping=True,    # Check if a connection is alive before using it
    future=True
)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Test the database connection
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Connected to the database successfully!")
    except Exception as e:
        print("❌ Connection failed")
        print(e)