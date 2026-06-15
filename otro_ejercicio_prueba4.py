
# Sistema de gestión de inventario
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Error: debe ingresar una opción entre 1 y 6.")
        except ValueError:
            print("Error: debe ingresar un número entero.")


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_precio(precio):
    return precio > 0


def validar_stock(stock):
    return stock >= 0


def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")

    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Error: el precio debe ser un número decimal.")
        return

    if not validar_precio(precio):
        print("Error: el precio debe ser mayor que cero.")
        return

    try:
        stock = int(input("Ingrese el stock del producto: "))
    except ValueError:
        print("Error: el stock debe ser un número entero.")
        return

    if not validar_stock(stock):
        print("Error: el stock debe ser mayor o igual a cero.")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "disponible": False
    }

    productos.append(producto)
    print("Producto agregado correctamente.")


def buscar_producto(productos, nombre_buscar):
    for i in range(len(productos)):
        if productos[i]["nombre"] == nombre_buscar:
            return i
    return -1


def actualizar_disponibilidad(productos):
    for producto in productos:
        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False

    print("Disponibilidad actualizada correctamente.")


def mostrar_productos(productos):
    actualizar_disponibilidad(productos)

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print("=== LISTA DE PRODUCTOS ===")

    for producto in productos:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")

        if producto["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN STOCK")

        print("*******************************************")


# Programa principal

productos = []
opcion = 0

while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_producto(productos)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        posicion = buscar_producto(productos, nombre)

        if posicion != -1:
            print(f"Producto encontrado en la posición {posicion}")
            print(f"Nombre: {productos[posicion]['nombre']}")
            print(f"Precio: ${productos[posicion]['precio']}")
            print(f"Stock: {productos[posicion]['stock']}")
            print(f"Disponible: {productos[posicion]['disponible']}")
        else:
            print("Producto no encontrado.")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        posicion = buscar_producto(productos, nombre)

        if posicion != -1:
            productos.pop(posicion)
            print("Producto eliminado correctamente.")
        else:
            print(f"El producto '{nombre}' no se encuentra registrado.")

    elif opcion == 4:
        actualizar_disponibilidad(productos)

    elif opcion == 5:
        mostrar_productos(productos)

    elif opcion == 6:
        print("Gracias por usar el sistema de inventario. Hasta pronto")