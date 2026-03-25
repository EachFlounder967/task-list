import sys
import json

with open("task-list.json", "r") as file:
    data = json.load(file)
tasks = data["tasks"]
header = "{:<6} {:<25} {:<12}, {:<30}, {:<10}".format(
    "Number", "Task", "Date Added", "Notes", "Priority"
)


def main():
    print("Hello from task-list!")
    print(header)
    print("-" * len(header))

    for row in tasks:
        print(
            "{:<6} {:<25} {:<12}, {:<30}, {:<10}".format(
                row["Number"],
                row["Task"],
                row["Date Added"],
                row["Notes"],
                row["Priority"],
            )
        )


if __name__ == "__main__":
    main()
