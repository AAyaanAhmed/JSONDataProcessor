import json

try:
    with open("employees.json", "r") as f:
        data = json.load(f)

    dep = input("Department: ").strip()

    total = 0
    count = 0

    print("\nEmployees")
    for i in data:
        if {"name", "department", "salary"} <= i.keys():
            if i["department"].lower() == dep.lower():
                print(i["name"], i["salary"])
                total += i["salary"]
                count += 1

    print("\nSummary")
    print("Count:", count)
    print("Total Salary:", total)
    print("Average:", total / count if count else 0)

except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError:
    print("Invalid JSON")
