from gestion_inventario import view_product, inventory

record_of_all_sales = [
    {"cliente" : "JUAN PEREZ", "tipo de cliente" : "Frequent customer", "producto vendido" : "Computador", "cantidad" : 1, "fecha de venta" : "2024-01-10", "descuento aplicado" : 10},
    {"cliente" : "MARIA LOPEZ", "tipo de cliente" : "Occasional customer", "producto vendido" : "Televisor", "cantidad" : 2, "fecha de venta" : "2024-01-12", "descuento aplicado" : 5},
    {"cliente" : "CARLOS GOMEZ", "tipo de cliente" : "Frequent customer", "producto vendido" : "Celular", "cantidad" : 3, "fecha de venta" : "2024-01-15", "descuento aplicado" : 12},
    {"cliente" : "ANA TORRES", "tipo de cliente" : "Frequent customer", "producto vendido" : "Licuadora", "cantidad" : 1, "fecha de venta" : "2024-01-18", "descuento aplicado" : 0},
    {"cliente" : "PEDRO MORA", "tipo de cliente" : "Occasional customer", "producto vendido" : "Lavadora", "cantidad" : 1, "fecha de venta" : "2024-01-20", "descuento aplicado" : 8},
    {"cliente" : "SOFIA MARTINEZ", "tipo de cliente" : "Frequent customer", "producto vendido" : "Celular", "cantidad" : 2, "fecha de venta" : "2024-01-22", "descuento aplicado" : 10},
    {"cliente" : "DANIEL ROJAS", "tipo de cliente" : "Occasional customer", "producto vendido" : "Computador", "cantidad" : 1, "fecha de venta" : "2024-01-25", "descuento aplicado" : 5},
    {"cliente" : "LAURA CASTILLO", "tipo de cliente" : "Frequent customer", "producto vendido" : "Televisor", "cantidad" : 1, "fecha de venta" : "2024-01-28", "descuento aplicado" : 15}
]

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
    product_sold = (input("Name of product sold: "))
    quantity = int(input("Quantity: "))
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
                    view_product(inventory)
                case 3:
                    break
                case _:
                    print("Invalid option")
        except ValueError:
            print("You must enter a number between 1 and 7")
