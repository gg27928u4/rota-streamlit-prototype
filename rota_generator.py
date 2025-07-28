
import pandas as pd
from collections import defaultdict

# Load CSV
staff_df = pd.read_csv("staff_preferences_template.csv")

# Define simple week structure
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
rota = defaultdict(list)

# Assign staff based on availability (basic example)
for day in days:
    for idx, row in staff_df.iterrows():
        available_days = row['Availability'].split(',')
        if day in available_days:
            rota[day].append(row["Name"])

# Output result
rota_df = pd.DataFrame(dict(rota)).T.fillna("")
rota_df.columns = [f"Slot {i+1}" for i in range(rota_df.shape[1])]
rota_df.index.name = "Day"
rota_df.to_csv("generated_rota.csv")
print("Rota saved as generated_rota.csv")
