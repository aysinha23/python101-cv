features = ["Dashboard", "Mobile App", "Checkout"]
active = True  # This is our 'Flag' to keep the loop running

while active:
    new_feature = input("\nAdd a feature (or type 'exit' to finish): ").strip()
    
    if new_feature.lower() == 'exit':
        active = False # This breaks the loop
    else:
        features.append(new_feature)
        print(f"Added! Current backlog size: {len(features)}")

# This only runs AFTER the loop finishes
print("\n--- FINAL SPRINT BACKLOG ---")
count = 0
for task in features:
    if len(task) >= 10:
        print(f"🔴 HIGH EFFORT: {task}")
        count += 1
    else:
        print(f"⚪ Task: {task}")

print(f"\nTotal High Effort Items: {count}")