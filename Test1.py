features=["Dashboard", "Mobile App", "Checkout"]

new_feature = input("Add new feature:").strip()

features.append(new_feature)

count = 0

for task in features:
    if len(task) > 10:
        print(f"HIGH EFFORT:{task}")
        count += 1


print(f"---SUMMARY----")
print(f"Total high effort features:{count}")
