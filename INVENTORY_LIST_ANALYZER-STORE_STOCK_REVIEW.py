print("Welcome to Inventory list Analyzer!")
print()

a = []

while True:
    item = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter Quantity: "))

    a.append({
        "Item": item,
        "Category": category,
        "Quantity": quantity
    })
    print()
    add = input("Do you want to add more items? (y/n): ")
    if add.lower() in ("n", "no"):
        print()
        break

print("========= Inventory Summary ===========")
print()


# Total items
total_items = len(a)
item_names = [i["Item"] for i in a]
print("Total Different Items: " ,total_items)
print("Explanation: You entered " ,total_items, " different items: " , ", ".join(item_names))


# Total quantity
quantities = [i["Quantity"] for i in a]
total_quantity = sum(quantities)
print("Total Quantity in Stock: " ,total_quantity)
print("Explanation: Sum of all quantities: " , " , ".join(str(q) for q in quantities) , " = " ,total_quantity)


# Average
average_quantity = total_quantity / total_items
print("Average Quantity per Item: " , round(average_quantity, 2))
print("Explanation: Average = " , total_quantity , " total / " , total_items , " items")


# Most stocked item
most_stocked = a[0]
least_stocked = a[0]

for i in a:
    if i["Quantity"] > most_stocked["Quantity"]:
        most_stocked = i
    if i["Quantity"] < least_stocked["Quantity"]:
        least_stocked = i

print("Most Stocked Item: " , most_stocked["Item"] ," (" ,most_stocked["Quantity"] , " units)")
print("Explanation: " , most_stocked["Item"] , " has the highest quantity among all items.")

print("Least Stocked Item: " , least_stocked["Item"] , " (" ,least_stocked["Quantity"] , " units)")
print("Explanation: " , least_stocked["Item"] , " has the lowest quantity.")


# Categories
print("----------------------------------\n")
unique_categories = sorted(set(i["Category"] for i in a))

print("Unique Categories in Inventory: " , str(unique_categories))
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")


#  Items sorted by quantity (descending)
print("----------------------------------")
print("📦 Items Sorted by Quantity (High to Low):")

sorted_items = a[:]

# Simple bubble sort (descending by Quantity)
for i in range(len(sorted_items)):
    for j in range(i , 1, len(sorted_items)):
        if sorted_items[i]["Quantity"] < sorted_items[j]["Quantity"]:
            sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]

count = 1
for i in sorted_items:
    print(str(count) , ". " , i["Item"] , " - " , str(i["Quantity"]) , " units")
    count += 1

print("\nExplanation: Items are sorted using the quantity field from highest to lowest.")

# Categories in alphabetical order
print("----------------------------------")
print("📂 Categories in Alphabetical Order:")

categories = sorted(set(i["Category"] for i in a))
count = 1
for c in categories:
    print(str(count) , ". " , c)
    count += 1

print("Explanation: The set of unique categories was sorted alphabetically for display.")

print("=========== END OF REPORT ===========")