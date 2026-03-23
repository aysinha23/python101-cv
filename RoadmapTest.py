# Run this once to create your test file
csv_content = """Task,Priority,Status
Login Page,High,Done
Checkout API,High,In Progress
Mobile App,Medium,To Do
Data Encryption,High,To Do
"""

with open("jira_export.csv", "w") as file:
    file.write(csv_content)

import csv

with open("jira_export.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Priority"] == "High" and row["Status"] == "To Do":
            print(f"🚨 URGENT: {row['Task']} needs a Kickoff!")

        
