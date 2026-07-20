customers = []


def add_customer():
    customer_id = int(input("Enter Customer ID: "))

    for customer in customers:
        if customer["CustomerId"] == customer_id:
            print("Customer ID already exists.")
            return

    name = input("Enter Customer Name: ")
    city = input("Enter City: ")

    customer = {
        "CustomerId": customer_id,
        "CustomerName": name,
        "City": city,
        "Orders": []
    }

    customers.append(customer)
    print("Customer Added Successfully.")


def add_order():
    customer_id = int(input("Enter Customer ID: "))

    for customer in customers:
        if customer["CustomerId"] == customer_id:

            product = {
                "ProductId": int(input("Enter Product ID: ")),
                "ProductName": input("Enter Product Name: "),
                "Quantity": int(input("Enter Quantity: ")),
                "Price": int(input("Enter Price: "))
            }

            customer["Orders"].append(product)
            print("Order Added Successfully.")
            return

    print("Customer not found.")


def view_customers():
    for customer in customers:
        print("\nCustomer ID :", customer["CustomerId"])
        print("Customer Name :", customer["CustomerName"])
        print("City :", customer["City"])

        print("\nOrders")

        if len(customer["Orders"]) == 0:
            print("No Orders")

        for order in customer["Orders"]:
            print("Product ID :", order["ProductId"])
            print("Product Name :", order["ProductName"])
            print("Quantity :", order["Quantity"])
            print("Price :", order["Price"])
            print()

        print("--------------------------------------")


def search_customer():
    customer_id = int(input("Enter Customer ID: "))

    for customer in customers:
        if customer["CustomerId"] == customer_id:

            print("\nCustomer ID :", customer["CustomerId"])
            print("Customer Name :", customer["CustomerName"])
            print("City :", customer["City"])

            print("\nOrders")

            if len(customer["Orders"]) == 0:
                print("No Orders")

            for order in customer["Orders"]:
                print("Product ID :", order["ProductId"])
                print("Product Name :", order["ProductName"])
                print("Quantity :", order["Quantity"])
                print("Price :", order["Price"])
                print()

            return

    print("Customer not found.")


def update_quantity():
    customer_id = int(input("Enter Customer ID: "))
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter New Quantity: "))

    for customer in customers:
        if customer["CustomerId"] == customer_id:

            for order in customer["Orders"]:
                if order["ProductId"] == product_id:
                    order["Quantity"] = quantity
                    print("Quantity Updated Successfully.")
                    return

            print("Product not found.")
            return

    print("Customer not found.")


def remove_product():
    customer_id = int(input("Enter Customer ID: "))
    product_id = int(input("Enter Product ID: "))

    for customer in customers:
        if customer["CustomerId"] == customer_id:

            for order in customer["Orders"]:
                if order["ProductId"] == product_id:
                    customer["Orders"].remove(order)
                    print("Product Removed Successfully.")
                    return

            print("Product not found.")
            return

    print("Customer not found.")


def total_bill():
    customer_id = int(input("Enter Customer ID: "))

    for customer in customers:
        if customer["CustomerId"] == customer_id:

            total = 0

            print()

            for order in customer["Orders"]:
                amount = order["Quantity"] * order["Price"]
                total += amount
                print(order["ProductName"], ":", amount)

            print("-----------------------")
            print("Total Bill :", total)
            return

    print("Customer not found.")


def max_order_value():
    max_customer = None
    max_total = 0

    for customer in customers:
        total = 0

        for order in customer["Orders"]:
            total += order["Quantity"] * order["Price"]

        if total > max_total:
            max_total = total
            max_customer = customer

    if max_customer:
        print("\nCustomer Name :", max_customer["CustomerName"])
        print("Total Amount :", max_total)


while True:

    print("\n===== Online Shopping Order Management System =====")
    print("1. Add New Customer")
    print("2. Add Product Order")
    print("3. View All Customers")
    print("4. Search Customer")
    print("5. Update Product Quantity")
    print("6. Remove Product")
    print("7. Calculate Total Order Value")
    print("8. Customer with Maximum Order Value")
    print("9. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_customer()

    elif choice == 2:
        add_order()

    elif choice == 3:
        view_customers()

    elif choice == 4:
        search_customer()

    elif choice == 5:
        update_quantity()

    elif choice == 6:
        remove_product()

    elif choice == 7:
        total_bill()

    elif choice == 8:
        max_order_value()

    elif choice == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")