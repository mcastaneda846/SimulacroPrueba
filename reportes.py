from registro_y_consulta_ventas import record_of_all_sales

def sort_by_quantity(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)

def build_product_sales_tuples(sales):
    sales_counter = {}   # diccionario para acumular ventas

    for sale in sales:
        product = sale["producto vendido"]
        quantity = int(sale["cantidad"])

        if product in sales_counter:
            sales_counter[product] += quantity
        else:
            sales_counter[product] = quantity

    result = [(product, total) for product, total in sales_counter.items()]
    return result

print(sort_by_quantity(build_product_sales_tuples(record_of_all_sales))[:3])