team_hours = {"Ayush": 35, "Sarah": 45, "Kevin": 30, "Matt": 50}

def check_sprint_health(hours_dict):
    overloaded_people = []
    for owner, hours in hours_dict.items():
        if hours > 40:
            overloaded_people.append(owner)
    return overloaded_people

burnout_list = check_sprint_health(team_hours)
print(f"Follow up with these people: {burnout_list}")
