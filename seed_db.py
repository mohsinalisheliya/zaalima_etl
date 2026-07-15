import pandas as pd
import random
from load.database import engine

print("🌱 Connecting to Supabase...")

# Create a list of realistic payment statuses with weighted probabilities
statuses = ["success", "failed", "pending", "refunded"]
weights = [70, 10, 15, 5] # 70% success rate

dummy_data = []

print("⚙️ Generating 100 dummy payment records...")
for i in range(100):
    dummy_data.append({
        "id": i + 50000, # Start at a high ID number to avoid conflicts
        "amount": round(random.uniform(15.00, 950.00), 2), # Random amounts between $15 and $950
        "status": random.choices(statuses, weights=weights)[0],
        "currency": "USD"
    })

# Convert to a Pandas DataFrame
df = pd.DataFrame(dummy_data)

try:
    # Push the dummy data directly into the Supabase 'payments' table
    print("🚀 Pushing data to the Data Warehouse...")
    df.to_sql("payments", engine, if_exists="append", index=False)
    print("✅ Successfully injected 100 dummy records into Supabase!")
except Exception as e:
    print(f"❌ Failed to seed database: {e}")