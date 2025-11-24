
inventory = [
    {"nombre del producto" : "Computador" , "marca" : "lenovo" , "categoría" : "portatiles" , "precio unitario" : 1500000 , "cantidad en stock": 10 , "garantía en meses" : 12},
    {"nombre del producto" : "Televisor" , "marca" : "LG" , "categoría" : "electrodoméstico" , "precio unitario" : 5500000 , "cantidad en stock": 15 , "garantía en meses" : 12},
    {"nombre del producto" : "Lavadora" , "marca" : "Haceb" , "categoría" : "electrodoméstico" , "precio unitario" : 240000 , "cantidad en stock": 2 , "garantía en meses" : 13},
    {"nombre del producto" : "Licuadora" , "marca" : "imusa" , "categoría" : "electrodoméstico" , "precio unitario" : 150000 , "cantidad en stock": 10 , "garantía en meses" : 12},
    {"nombre del producto" : "Celular" , "marca" : "iphone" , "categoría" : "movil" ,"precio unitario" : 5500000 , "cantidad en stock": 40 , "garantía en meses" : 24}
]


def add_product() :
    print("\nEnter the product details\n")
    
    while True:
        product_name = input("Product name: ").strip().upper()
        if not product_name:
            print("The field cannot be left empty.")
            continue
        elif not product_name.replace(" ","").isalpha():
            print("Please enter only text")
            continue
        break

    while True:
        brand = input("Product brand: ").strip().upper()
        if not brand:
            print("The field cannot be left empty.")
            continue
        elif not brand.replace(" ","").isalpha():
            print("Please enter only text")
            continue
        break

    while True:
        category = input("Product category: ").strip().upper()
        if not category:
            print("The field cannot be left empty.")
            continue
        elif not category.replace(" ","").isalpha():
            print("Please enter only text")
            continue
        break
    
    while True:
        unit_price = input("Precio unitario: ").strip().upper()
        if not unit_price:
            print("The field cannot be left empty.")
            continue

        try:
            unit_price = float(unit_price)
        except ValueError:
            print("You must enter a number")
            continue
        if unit_price <= 0:
            print("The price must be greater than 0")
            continue
        break

    while True:
        quantity_in_stock = input("Quantity in stock: ").strip().upper()
        if not quantity_in_stock:
            print("The field cannot be left empty.")
            continue

        try:
            quantity_in_stock = float(quantity_in_stock)
        except ValueError:
            print("You must enter a number")
            continue
        if quantity_in_stock <= 0:
            print("The price must be greater than 0")
            continue
        break

    while True:
        warranty = input("warranty: ").strip().upper()
        if not warranty:
            print("The field cannot be left empty.")
            continue

        try:
            warranty = float(warranty)
        except ValueError:
            print("You must enter a number")
            continue
        if warranty <= 0:
            print("The price must be greater than 0")
            continue
        break


    product = {
        "nombre del producto" : product_name,
        "marca" : brand,
        "categoría" : category,
        "precio unitario" : unit_price,
        "cantidad en stock" : quantity_in_stock,
        "garantía en meses" : warranty
        }

    inventory.append(product)

def view_product(inventory):
    for item in inventory:
        print(item)

    while True:
        product_name = input("\nSearch by product name: ").lower().strip()

        if not product_name:
            print("The field cannot be left empty.")
            continue
        elif not product_name.replace(" ","").isalpha():
            print("Please enter only text")
            continue
        break

    for item in inventory:
        if item['nombre del producto'].lower() == product_name:
            print(f"\nProduct name: {item['nombre del producto']} | Brand: {item['marca']} | "
                  f"Category: {item['categoría']} | Unit price: {item['precio unitario']} | "
                  f"Stock quantity: {item['cantidad en stock']} | Warranty (months): {item['garantía en meses']}")
            break
    else:
        print("\nNo product found with that name")
    return

def update_products(inventory) :

    while True:
        search_product = input("\nEnter the name of the product you are looking for: ")

        if not search_product:
            print("The field cannot be left empty.")
            continue
        elif not search_product.replace(" ","").isalpha():
            print("Please enter only text")
            continue
        break

    for item in inventory:

        if item['nombre del producto'].lower() == search_product.lower():
        # New price
            while True:
                try:
                    new_unit_price = float(input(f"Nuevo precio para {item['nombre del producto']}: "))
                    if new_unit_price < 0:
                        print("El precio debe ser positivo.")
                        continue
                    break
                except ValueError:
                    print("Ingrese un precio válido.")
                        # Nueva cantidad
            while True:
                try:
                    new_quantity_in_stock = int(input(f"Nueva cantidad para {item['nombre del producto']}: "))
                    if new_quantity_in_stock < 0:
                        print("La cantidad debe ser positiva.")
                        continue
                    break
                except ValueError:
                    print("Ingrese una cantidad válida.")
                
            # Actualizar
            item['precio unitario'] = new_unit_price
            item['cantidad en stock'] = new_quantity_in_stock
            print(f"Producto {item['nombre del producto']} actualizado: Unit price : {new_unit_price}, Quantity in stock: {new_quantity_in_stock}\n")
            return  # Fin de la función al actualizar

    print("No se encontró el producto.\n")


def eliminar_producto(inventory, name = None):

    while True:
        if not name:
            name = input("Ingrese el nombre del producto a eliminar: ")

        # Validación: no vacío y solo letras y espacios
        if not name.strip() or not name.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras y no puede estar vacío.")
            name = None
            continue  # Repite la entrada
        break  # Nombre válido, salir del bucle

    # Buscar y eliminar
    for item in inventory:
        if item['nombre del producto'].lower() == name.lower():
            inventory.remove(item)
            print(f"El producto '{item['nombre del producto']}' se eliminó correctamente.\n")
            return
    print("No se encontró el producto.\n")



