task = input("Enter your task:")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task", end="")
    case "low":
        print(f"Note: '{task}' is a low priority task", end="")
    case _:
        print("Invalid priority entered.")
        exit()

if time_bound == "yes":
    print(" that requires immediate attention today!")
elif time_bound == "no":
    print(". Consider completing it when you have free time.")


