import csv

print("Canteen Sales Data Analysis")
print("----------------------------")

total_revenue = 0
highest_quantity = 0
best_item = ""
category_sales = {}

with open("sales.csv", "r") as file:

    data = csv.DictReader(file)

    for row in data:

        # Read data from CSV
        quantity = int(row["Quantity"])
        price = float(row["Price"])
        item = row["Item"]
        category = row["Category"]

        # Calculate revenue for each item
        revenue = quantity * price

        # Add revenue to total revenue
        total_revenue = total_revenue + revenue

        # Find best-selling item
        if quantity > highest_quantity:
            highest_quantity = quantity
            best_item = item

        # Calculate category-wise revenue
        if category not in category_sales:
            category_sales[category] = 0

        category_sales[category] = category_sales[category] + revenue

        # Display item revenue
        print(item, "-> ₹", revenue)


print("----------------------------")
print("Total Revenue =", total_revenue)
print("Best Selling Item =", best_item)
print("Quantity Sold =", highest_quantity)

print("\nCategory-wise Revenue:")

for category in category_sales:
    print(category, "=", category_sales[category])
