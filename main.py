import datetime

count = 0
greeted = []

while True:
    name = input("What is your name? (or 'quit' to exit, 'list' to see greeted names, 'delete' to remove a name) ")
    if name.lower() == "quit":
        with open("greeted_names.txt", "w") as f:
            for entry in greeted:
                f.write(entry + "\n")
        print(f"Goodbye! Have a great day! ({count} people greeted)")
        print("Names saved to greeted_names.txt")
        break
    if name.lower() == "list":
        if greeted:
            print("\nPeople greeted so far:")
            for entry in greeted:
                print(f"  - {entry}")
        else:
            print("No one has been greeted yet.")
        print()
        continue
    if name.lower() == "delete":
        if not greeted:
            print("No one has been greeted yet.")
            print()
            continue
        print("\nPeople greeted so far:")
        for i, entry in enumerate(greeted, 1):
            print(f"  {i}. {entry}")
        delete_input = input("Enter the number to delete (or 'cancel'): ")
        if delete_input.lower() != "cancel":
            try:
                index = int(delete_input) - 1
                if 0 <= index < len(greeted):
                    removed = greeted.pop(index)
                    count -= 1
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Invalid input.")
        print()
        continue
    while True:
        age_input = input("How old are you? ")
        try:
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid age. Please enter a number.")
    count += 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    greeted.append(f"{name}, age {age} (greeted at {timestamp})")
    print(f"Hello, {name}! You are {age} years old.")
    print()
