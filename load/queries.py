import pandas as pd
from load.database import engine

def fetch_dashboard_data():
    query = "SELECT status, SUM(amount) as total FROM payments GROUP BY status"
    return pd.read_sql(query, engine)