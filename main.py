import datetime

count = 0
greeted = []

while True:
    name = input("What is your name? (or 'quit' to exit, 'list' to see greeted names) ")
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
