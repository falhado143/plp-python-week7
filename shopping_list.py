
# Week 7 Assignment: Shopping List Manager

shopping_list = []

while True:
    print("\n===== SHOPPING LIST MANAGER =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "has been added.")
        else:
            print("Please enter a valid item.")

    elif choice == "2":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print(item, "is not in the shopping list.")

    elif choice == "3":
        if shopping_list:
            print("\nYour Shopping List:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Thank you for using Shopping List Manager!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
