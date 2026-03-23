def calculate_velocity(total_points, days_in_sprint):
    velocity = total_points/days_in_sprint
    return velocity

my_velocity = calculate_velocity(40, 10)

print(f"Our daily veloctiy is: {my_velocity}")

