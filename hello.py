backlog = ["Fix Login Bug", "Update UI", "API Bug - critical", "Database Cleanup", "Write Docs"]

bug_count = 0  # Using a descriptive name instead of 'x' helps others understand your code

for task in backlog:
    if "Bug" in task:
        print(f"🔴 Found a bug: {task}")
        bug_count += 1 

print(f"\n--- SUMMARY ---")
print(f"Total tasks with Bugs: {bug_count}")

#Day 2 - Starting dictionaries
