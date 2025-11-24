from gestion_inventario import * 
from registro_y_consulta_ventas import *
from reportes import generar_reportes


while True: 

    try:
        print("\n-----INTEGRATED INVENTORY AND SALES MANAGEMENT SYSTEM-----\n")

        print("Select a number according to the required option\n"
            "\n1. Add product."
            "\n2. Consult products."
            "\n3. Update product."
            "\n4. Delete product."
            "\n5. Sales registration and inquiry."
            "\n6. Reports")


        option = int(input("Enter your choice: "))

        match option:
            case 1:
                add_product()
            case 2:
                print("\n-----CONSULT PRODUCTS -----\n")
                view_product(inventary)
            case 3:
                print("-------UPDATE PRODUCTS-------")
                update_products(inventary)
            case 4: 
                print("\n-------DELETE PRODUCT-------\n")
                eliminar_producto(inventary, name = None)
            case 5:
                sales_menu()
            case 6:
                generar_reportes()
            case _:
                print("invalid option")

    except ValueError :
        print("You must enter a number between 1 and 7")

