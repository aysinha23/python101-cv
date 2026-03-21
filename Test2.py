bugs = ["Login Error", "Slow Loading", "UI Glitch"]

while len(bugs)>0:
    print(f"Current Bugs: {bugs}")
    bug_fixed = input("Which bug did you fix:").strip()
    bugs.remove(bug_fixed)

print(f"Sprint Complete: All Bugs have been fixed ✅!")