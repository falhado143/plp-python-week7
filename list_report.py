
# Week 7 Assignment: Shopping List Report

shopping_list = [
    "Rice",
    "Sugar",
    "Milk",
    "Bread",
    "Eggs",
    "Cooking Oil"
]

# Display the shopping list
print("===== SHOPPING LIST REPORT =====")

print("\nItems in your shopping list:")

for item in shopping_list:
    print("-", item)

# Count the items
total_items = len(shopping_list)

print("\nTotal number of items:", total_items)

# Check whether a specific item exists
if "Milk" in shopping_list:
    print("Milk is on the shopping list.")
else:
    print("Milk is not on the shopping list.")

# Display a message based on the number of items
if total_items == 0:
    print("Your shopping list is empty.")
elif total_items <= 5:
    print("You have a short shopping list.")
else:
    print("You have a long shopping list.")

print("\nEnd of report.")
