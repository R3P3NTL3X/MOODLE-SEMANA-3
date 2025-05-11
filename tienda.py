nombre_cliente=input("Cual es tu nombre?")
print(f"BIENVENIDO {nombre_cliente} A NUESTRA TIENDA VIRTUAL.")

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
        return
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        if precio < 0 or cantidad < 0:
            print("El precio y la cantidad deben ser valores positivos.")
            return
        inventario[nombre] = (precio, cantidad)
        print(f"Producto '{nombre}' añadido exitosamente.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido para precio y cantidad.")

def consultar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a consultar: ").strip()
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
    else:
        print("El producto no está en el inventario.")

def actualizar_precio(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre in inventario:
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio < 0:
                print("El precio debe ser un valor positivo.")
                return
            cantidad = inventario[nombre][1]
            inventario[nombre] = (nuevo_precio, cantidad)
            print(f"Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}")
        except ValueError:
            print("Error: Ingrese un valor numérico válido para el precio.")
    else:
        print("El producto no está en el inventario.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print("El producto no está en el inventario.")

def calcular_valor_total(inventario):
    calcular_producto = lambda precio, cantidad: precio * cantidad
    total = sum(calcular_producto(precio, cantidad) for precio, cantidad in inventario.values())
    print(f"El valor total del inventario es: ${total:.2f}")

def mostrar_menu():
    print("\n--- ¿QUE QUIERES HACER EL DIA DE HOY? ---")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario completo")
    print("7. Salir")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nInventario actual:")
        for nombre, (precio, cantidad) in inventario.items():
            print(f"- {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")

# Programa principal
def main():
    inventario = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            consultar_producto(inventario)
        elif opcion == '3':
            actualizar_precio(inventario)
        elif opcion == '4':
            eliminar_producto(inventario)
        elif opcion == '5':
            calcular_valor_total(inventario)
        elif opcion == '6':
            mostrar_inventario(inventario)
        elif opcion == '7':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
