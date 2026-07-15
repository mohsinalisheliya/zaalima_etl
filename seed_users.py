import pandas as pd
import random
from load.database import engine

print("🌱 Connecting to Supabase...")

# Lists to generate realistic dummy data
first_names = ["Ali", "Sara", "John", "Priya", "Rahul", "Aisha", "Michael", "Emma"]
last_names = ["Khan", "Smith", "Patel", "Sharma", "Williams", "Brown", "Ali", "Davis"]
domains = ["gmail.com", "zaalima.com", "yahoo.com", "techcorp.io"]

dummy_users = []

print("⚙️ Generating 15 dummy users...")
for i in range(15):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first.lower()}.{last.lower()}{random.randint(10,99)}@{random.choice(domains)}"
    
    dummy_users.append({
        "name": f"{first} {last}",
        "email": email
    })

df = pd.DataFrame(dummy_users)

try:
    print("🚀 Pushing users to the Data Warehouse...")
    # Note: We don't include 'id' because the database will auto-generate it!
    df.to_sql("users", engine, if_exists="append", index=False)
    print("✅ Successfully injected 15 dummy users into Supabase!")
except Exception as e:
    print(f"❌ Failed to seed users: {e}")