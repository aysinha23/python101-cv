import csv
import matplotlib.pyplot as plt

# 1. Data Buckets
categories = []
counts = []

# 2. Read the CSV
with open("warehouse_inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        categories.append(row["Item"])
        counts.append(int(row["Count"]))

# 3. Create the Chart
plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color='skyblue')

# 4. Add the labels
plt.title("Amazon Fresh: Inventory Levels by Item")
plt.xlabel("Items")
plt.ylabel("Units in Stock")
plt.xticks(rotation=45) # Tilt the labels so they don't overlap

# 5. Save it!
plt.tight_layout()
plt.savefig("inventory_report.png")
print("📈 Success! Check your folder for inventory_report.png")