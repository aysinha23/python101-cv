roadmap = {
    "Login Bug": {"owner": "Ayush", "priority": "High", "status": "In Progress"},
    "Checkout UI": {"owner": "Sarah", "priority": "Medium", "status": "To Do"},
    "API Docs": {"owner": "Kevin", "priority": "Low", "status": "Done"}
}

# To see just the priority of the Login Bug:
print(f"Priority: {roadmap['Login Bug']['priority']}")

roadmap["Mobile App"] = {"owner":"Engineering", "status": "Done"}

for task,details in roadmap.items():
    if details["status"] == "Done":
        print(f"✅ Completed: {task}; Assigned to: {details["owner"]}")
    else:    
        print(f"⏳ PENDING: {task}; Assigned to: {details['owner']}")

