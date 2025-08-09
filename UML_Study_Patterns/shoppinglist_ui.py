# Dictionary to define to screen prototypes
prototype_screens = {
    "My Shopping Lists": {
        "No_of_Screens": 1,
        "flows_to": ["Groceries"],
        "Page": 1
    },
    "Groceries": {
        "No_of_Screens": 1,
        "flows_to": ["Add Item", "Edit Item", "Delete Item"],
        "Page": 2
    },
    "Add Item": {
        "No_of_Screens": 1,
        "flows_to": ["Groceries"],
        "Page": 3
    },
    "Edit Item": {
        "No_of_Screens": 1,
        "flows_to": ["Groceries"],
        "Page": 4
    },
    "Delete Item": {
        "No_of_Screens": 1,
        "flows_to": ["Groceries"],
        "Page": 5
    }
}

# Print screen names, count of screens and flow sequence
print("Prototype Page Summary:\n")
total_pages = 0

for screen, details in prototype_screens.items():
    print(f"Screen: {screen}")
    print(f"  No_of_Screens: {details['No_of_Screens']}")
    print(f"  Flows to: {', '.join(details['flows_to'])}")
    print(f"  Screen Number: {details['Page']}")
    total_pages += details['No_of_Screens']
    print()

print(f"Total number of pages in prototype: {total_pages}")
