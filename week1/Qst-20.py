shopping_list = []

while True:
    action = input("What would you like to do? (add/remove/show/quit): ")

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    elif action == "show":
        print("Current shopping list:")

    elif action == "quit":
        print("Exiting the shopping list manager. Goodbye!")
        break

    else:
        print("Invalid action. Please choose add, remove, show, or quit.")