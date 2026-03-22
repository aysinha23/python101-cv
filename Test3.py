team_hours = {
    "Ayush": 35,
    "Sarah": 42,
    "Kevin": 28
}

team_hours["Ayush"] = 40
team_hours["Engineering Manager"] = 10

for name, hours in team_hours.items():
    if team_hours[name] > 40:
        print(f"⚠️ OVER CAPACITY; Name:{name}; Hours: {hours}")
    else:
        print(f"✅ Within Limits; Name:{name}; Hours: {hours}")