def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if minimo is not None and numero < minimo:
                print(f"Debe ser un número entero mayor o igual a {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"Debe ser un número entero menor o igual a {maximo}.")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un número entero válido.")


def leer_float(mensaje, minimo=None, maximo=None):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = float(valor)
            if minimo is not None and numero < minimo:
                print(f"Debe ser un número mayor o igual a {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"Debe ser un número menor o igual a {maximo}.")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un número válido.")


def agregar_producto(productos):
    nombre = input("Ingrese nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    if nombre in productos:
        print("Ese producto ya existe.")
        return

    stock = leer_entero("Ingrese stock: ", minimo=0)
    precio = leer_float("Ingrese precio: ", minimo=1)

    productos[nombre] = [stock, precio]
    print("Producto agregado correctamente.")


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    print("\n--- Productos registrados ---")
    for nombre, datos in productos.items():
        stock = datos[0]
        precio = datos[1]
        print(f"Producto: {nombre} | Stock: {stock} | Precio: ${precio}")


def buscar_producto(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    nombre = input("Ingrese el nombre del producto a buscar: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    if nombre in productos:
        print(f"El producto {nombre} existe.")
        print(f"Stock: {productos[nombre][0]} | Precio: ${productos[nombre][1]}")
    else:
        print("El producto no existe.")


def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    nombre_caro = ""
    precio_mayor = 0

    for nombre, datos in productos.items():
        precio = datos[1]
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_caro = nombre

    print(f"El producto más caro es {nombre_caro}, con precio ${precio_mayor}.")


def mostrar_menu():
    print("\n--- MENÚ INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto más caro")
    print("5. Salir")


def main():
    productos = {}

    while True:
        mostrar_menu()
        opcion = leer_entero("Ingrese opción: ", minimo=1, maximo=5)

        if opcion == 1:
            agregar_producto(productos)
        elif opcion == 2:
            mostrar_productos(productos)
        elif opcion == 3:
            buscar_producto(productos)
        elif opcion == 4:
            producto_mas_caro(productos)
        elif opcion == 5:
            print("Programa finalizado.")
            break


main()
