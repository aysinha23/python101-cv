import csv

# 1. Our Logic (The Tool)
def check_sprint_health(hours_dict):
    overloaded = []
    for name, hours in hours_dict.items():
        if int(hours) > 40: # Note: CSV data always starts as a String!
            overloaded.append(name)
    return overloaded

# 2. Reading the File (The Data)
current_team_hours = {}

with open("sprint_data.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # row is a dictionary: {'Name': 'Ayush', 'Hours': '40'}
        current_team_hours[row["Name"]] = row["Hours"]

# 3. Running the Report
burnout_list = check_sprint_health(current_team_hours)
print(f"🚨 ACTION REQUIRED: Follow up with {burnout_list}")