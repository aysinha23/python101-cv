# Random Inventory Levels
inventory_data = """Item,Status,Count,Category
Organic Bananas,In Stock,450,Produce
Oat Milk,Low Stock,12,Dairy
Avocados,Out of Stock,0,Produce
Paper Towels,In Stock,1200,Household
Whole Milk,Out of Stock,0,Dairy
Protein Bars,Low Stock,5,Snacks
"""

with open("warehouse_inventory.csv", "w") as file:
    file.write(inventory_data)

print("✅ warehouse_inventory.csv created with 6 items.")

import csv
import requests

# 1. PASTE WEBHOOK HERE
SLACK_WEBHOOK_URL = "XYZ" 

def send_slack_alert1(item_name, category):
    payload = {
        "text": f"----- *AMAZON FRESH STOCK ALERT* -----\n*Item:* {item_name}\n*Category:* {category}\n*Status:* URGENT! OUT OF STOCK 🚫"
    }
    requests.post(SLACK_WEBHOOK_URL, json=payload)

def send_slack_alert2(item_name, category):
    payload = {
        "text": f"----- *AMAZON FRESH STOCK ALERT* -----\n*Item:* {item_name}\n*Category:* {category}\n*Status:* Low Stock Warning! ⚠️"
    }
    requests.post(SLACK_WEBHOOK_URL, json=payload)

LOW_STOCK_THRESHOLD = 20

# 2. The Processing Loop to call function based on inventory levels
with open("warehouse_inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # PM Logic: If Count is 0, trigger the Slack notification
        if int(row["Count"]) == 0:
            send_slack_alert1(row["Item"], row["Category"])
            print(f"📡 OOS Alert dispatched for: {row['Item']}")
        elif int(row["Count"]) <= LOW_STOCK_THRESHOLD and int(row["Count"]) > 0:
            send_slack_alert2(row["Item"], row["Category"])
            print(f"📡 Low Stock Alert dispatched for: {row['Item']}")



