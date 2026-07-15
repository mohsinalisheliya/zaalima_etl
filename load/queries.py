import pandas as pd
from load.database import engine

def fetch_dashboard_data():
    query = "SELECT status, SUM(amount) as total FROM payments GROUP BY status"
    return pd.read_sql(query, engine)

# ✨ NEW: Pulls every individual record from the database
def fetch_raw_data():
    query = "SELECT * FROM payments"
    return pd.read_sql(query, engine)

# ✨ NEW: Pulls the user directory from the database
def fetch_users_data():
    query = "SELECT * FROM users"
    return pd.read_sql(query, engine)