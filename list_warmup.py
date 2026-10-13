
# Week 7 Assignment: Shopping List Manager

shopping_list = ["Rice", "Sugar", "Milk", "Bread", "Eggs"]

# Print the complete shopping list
print("My Shopping List:")
print(shopping_list)

# Print the first item
print("\nFirst item:", shopping_list[0])

# Print the third item
print("Third item:", shopping_list[2])

# Add a new item
shopping_list.append("Cooking Oil")
print("\nAfter adding Cooking Oil:")
print(shopping_list)

# Remove an item
shopping_list.remove("Sugar")
print("\nAfter removing Sugar:")
print(shopping_list)

# Check if an item exists
if "Milk" in shopping_list:
    print("\nMilk is in the shopping list.")
else:
    print("\nMilk is not in the shopping list.")
