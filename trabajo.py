"""
    La tienda de venta de artículos de regalo “gifty”, lleva su control de inventario a través de hojas
    de Excel, registrando las entradas de artículos y salidas de cada uno cada vez que se vende un
    artículo. Ustedes como equipo de desarrolladores de software en Python deben desarrollar un
    sistema sencillo de gestión de inventario. El sistema permitirá a los usuarios administrar el
    inventario de la tienda, utilizando los conceptos aprendidos en las cuatro unidades del
    diplomado en Python, incluyendo el uso de variables, estructuras de control de flujo, funciones
    y módulos, y estructuras de datos.

    ¿Qué deben hacer?
    1) Interfaz: El sistema tendrá una interfaz de texto intuitiva donde los usuarios puedan
    interactuar con el programa mediante la selección de opciones de un menú.

    2) Gestión de Productos: El programa permitirá a los usuarios agregar nuevos productos al
    inventario, actualizar la información de los productos existentes y eliminar productos del
    inventario.

    3) Visualización del Inventario: El programa mostrará una lista de todos los productos en el
    inventario, con información detallada sobre cada producto, como nombre, precio, cantidad
    disponible, etc.

    4) Búsqueda de Productos: El sistema permitirá a los usuarios buscar productos en el
    inventario por su nombre o código, facilitando la ubicación y actualización de productos
    específicos.

    5) Control de Stock: El programa controlará el stock de los productos, alertando al usuario
    cuando un producto esté bajo en cantidad para que puedan tomar acciones preventivas.

    6) Generación de Reportes: El sistema generará reportes periódicos sobre el estado del
    inventario, incluyendo el total de productos, productos más vendidos, productos con stock
    bajo, etc
"""
import os
# lista inventario almacenar el invetario en memoria producto, cantidad y precio
inventario = []

# lista ventas almacenar las ventas memoria producto y venta
ventas = []

"Interfaz tienda  GIFTY "


def Tienda():
    while True:
        os.system('cls')
        
        print("_______________________________________________________________")
        print("\nTienda de regalos GIFTY, seleccione una OPCION para continuar")
        print("_______________________________________________________________")
        print("1. Mostrar inventario")
        print("2. Mostrar ventas")
        print("3. Agregar artículo")
        print("4. Vender artículo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Mostrar_inventario()

        elif opcion == "2":
            Mostrar_venta()

        elif opcion == "3":
            os.system('cls')
            producto = input("Ingrese el nombre del artículo: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            precio = int(input("Ingrese precio unitario : "))
            Agregar_Articulo(producto, cantidad, precio)
        elif opcion == "4":            
            os.system('cls')
            producto = input("Ingrese el nombre del artículo a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            Vender_Articulo(producto, cantidad)
        elif opcion == "5":
            print("Salir")
            break

        else:
            os.system('cls')
            print("Opción no válida. Intente de nuevo.")
            input('Pulse una tecla para continuar...')


# Funcion listar inventario
def Mostrar_inventario():
    
    os.system('cls')
    print('Inventario')
    print("_______________________________________________________________")
    for i in range(len(inventario)):
        print(inventario[i])
    if len(inventario) == 0:
        print("No se registran productos")
    input('Pulse una tecla para continuar...')

# Funcion listar ventas y mostrar la venta con mayor ganancia
def Mostrar_venta():
    os.system('cls')
    print('Ventas')
    print("_______________________________________________________________")
    van = 0
    for i in range(len(ventas)):
        print(ventas[i])
        mejor_venta = max(ventas, key=lambda x: x[1])
        van = + 1
    if van == 0:
        print("No se registran ventas")
    else:
        print(" Mejor Venta:", mejor_venta[1])
    input('Pulse una tecla para continuar...')
# Funcion agregar inventario


def Agregar_Articulo(producto_A, cantidad_A, precio_A):
    # Validar si el producto existe
    for i, (producto, cantidad, precio) in enumerate(inventario):
        if producto == producto_A:

            print("Producto :", producto)
            print("Inventario actual :", cantidad)
            print("Productos a ingresar :", cantidad_A)
            print("Precio  unitario $ :", cantidad_A)

            nuevo_inventario = int(cantidad)+int(cantidad_A)
            inventario[i] = (producto, nuevo_inventario, precio_A)
            break
    # Si el producto no existe
    else:
        producto = producto_A
        cantidad = cantidad_A
        precio = precio_A
        os.system('cls')
        print("Nuevo producto :", producto)
        print("Cantidad :", cantidad)
        print("Precio $:", precio)

        inventario.append((producto, cantidad, precio))
        input('Pulse una tecla para continuar...')

# Funcion vender inventario
def Vender_Articulo(producto_V, cantidad_V):
    for i, (producto, cantidad, precio) in enumerate(inventario):
        if producto == producto_V:

            print("Producto :", producto)
            print("Cantidad inventario:", cantidad)
            print("cantidad Venta $:", cantidad_V)

            nuevo_inventario = int(cantidad)-int(cantidad_V)

            if (nuevo_inventario < 0):
                print("inventario insuficiente")
                input('Pulse una tecla para continuar...')
                break
            else:
                venta = cantidad_V * precio
                print("Venta Procesada $ ", venta)
                inventario[i] = (producto, nuevo_inventario, precio)

                ventas.append((producto, venta))
                input('Pulse una tecla para continuar...')
                break
    else:
        print("Producto no encontrado")
        input('Pulse una tecla para continuar...')


Tienda()