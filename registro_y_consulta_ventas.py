from gestion_inventario import view_product, inventary

record_of_all_sales = []

def sales_record():
    customer = input("Customer name:").upper()
    customer_type = int(input("Press 1 for frequent customer or 2 for occasional customer: "))
    if customer_type == 1:
        customer_type = "Frequent customer"
        print(customer_type)
    elif customer_type == 2:
        customer_type = "Occasional customer"
        print(customer_type)
    else:
        print("Valor no válido")
    product_sold = input("Name of product sold: ")
    quantity = input("Quantity: ")
    sales_date = input("Sales date: ")
    discount_applied = int(input("Discount applied: "))

    sales = {
        "cliente" : customer,
        "tipo de cliente" : customer_type,
        "producto vendido" : product_sold,
        "cantidad" : quantity,
        "fecha de venta" : sales_date,
        "descuento aplicado" : discount_applied
        
    }
    record_of_all_sales.append(sales)

def sales_menu():

    while True:
        try:
            print("\n-----INTEGRATED INVENTORY AND SALES MANAGEMENT SYSTEM-----\n")

            print("Select a number according to the required option\n"
                "\n1. Add product."
                "\n2. Consult products."
                "\n3. Return to the main menu.")
            
            option = int(input("Enter your choice: "))

            match option:
                case 1:
                    print("\n-------SALES RECORD-------\n")
                    sales_record()
                case 2:
                    print("\n-----CONSULT PRODUCTS -----\n")
                    view_product(inventary)
                case 3:
                    break
                case _:
                    print("Invalid option")
        except ValueError:
            print("You must enter a number between 1 and 7")
