# 1. Create a dummy CSV file for our test
content = "Name,Hours\nAyush,40\nSarah,45\nKevin,30\nMatt,50"

with open("sprint_data.csv", "w") as file:
    file.write(content)

print("✅ File 'sprint_data.csv' created successfully!")