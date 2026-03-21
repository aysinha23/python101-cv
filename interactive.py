backlog = ["Fix Login Bug", "Update UI", "API Bug"]

# 1. Ask the user for input
new_task = input("Enter a new task for the backlog: ")

# 2. Add it to our list
backlog.append(new_task)

print(f"\n--- UPDATED BACKLOG ({len(backlog)} total) ---")

bug_count = 0
for task in backlog:
    if "bug" in task.lower():
        print(f"🔴 BUG: {task}")
        bug_count += 1
    else:
        print(f"⚪ Task: {task}")

print(f"\nTotal Bugs Found: {bug_count}")