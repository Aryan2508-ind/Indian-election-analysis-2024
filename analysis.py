import pandas as pd

# 1. DATA INGESTION (Step 01: Dashboard ke according)
try:
    # Ye line aapki 'eci_results_2024.csv' file ko read karegi
    df = pd.read_csv('eci_results_2024.csv')
    print("Step 01: Data successfully loaded!")
except Exception as e:
    print("Error: CSV file nahi mili ya khali hai.")
    # Agar file khali hai toh ye sample data create karega testing ke liye
    data = {
        'party': ['BJP', 'INC', 'SP', 'BJP', 'INC', 'AITC', 'BJP', 'SP'],
        'margin': [150000, 20000, 50000, 120000, 45000, 80000, 200000, 10000]
    }
    df = pd.DataFrame(data)

# 2. DEDUPLICATION & CLEANING (Step 02 & 03)
# Duplicate entries hatana
df = df.drop_duplicates()

# Party names se extra space hatana
df['party'] = df['party'].str.strip()

# 3. ANALYSIS (Step 04: Seats Calculation)
# Har party ne kitni seats jeeti wo count karna
seat_counts = df['party'].value_counts()

print("\n--- ANALYSIS COMPLETE ---")
print(seat_counts)

# 4. EXPORT FOR HTML (Step 05)
# Ye output aapko copy karke index.html ke <script> section mein dalna hota hai
print("\n--- Copy this into your index.html <script> ---")
for party, seats in seat_counts.items():
    print(f"{{ name: '{party}', seats: {seats} }},")