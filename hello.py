# A List of tasks
tasks = ["Email the dev team", "Review PRs", "Update roadmap", "Sprint planning"]

print("--- MY TO-DO LIST ---")

# A Loop to print each task with its length
for task in tasks:
    # len() counts the characters in a string
    task_length = len(task)
    print(f"Task: {task} ({task_length} characters)")

# Adding a new task to the list
tasks.append("Go to the gym")
print(f"\nTotal tasks now: {len(tasks)}")