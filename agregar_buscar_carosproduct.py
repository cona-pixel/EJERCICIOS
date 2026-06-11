productos= {
    "Mouse" : [10,15000],
    "Teclado" : [5, 25000],
    "Monitor" : [3, 180000]
}

def agregar_productos(productos):
        nombre=input("Ingresa el nombre del producto: ").strip().lower()
        if nombre == "":
            print("El nombre no puede estar vacio.")
            return
        if nombre in productos:
            print("El producto ya existe!!!")
            return
        
        stock=int(input("Ingresa el stock del producto: "))
        precio=int(input("Ingresa el precio: "))

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

        print(f"Producto: {nombre}")
        print(f"Stock: {stock}")
        print(f"Precio: ${int(precio)}")
        print("--------------------")
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

    print(f"El producto más caro es el {nombre_caro}, su precio es ${precio_mayor}.")
def buscar_productos(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    nombre = input("Ingrese el producto que desea buscar: ").strip().lower()
    while True:
        nombre = input("Ingrese el producto que desea buscar: ").strip().lower()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        if nombre in productos:
            print(f"El producto {nombre} existe.")
            print(f"Stock: {productos[nombre][0]}")
            print(f"Precio: ${int(productos[nombre][1])}")
            break
        else:
            print("El producto no existe.Debe escribir bien el nombre del producto.")
            print("Productos disponibles: ")

            for producto in productos:
                print("-", producto)

while True:
    print("---------MENU-------")
    print("1.Agregar producto")
    print("2.Mostrar productos")
    print("3.Buscar productos")
    print("4.Producto mas caro")
    print("5.Salir")

    while True:
        try:
            op=int(input("Ingrese la opción: "))
            if op < 1 or op > 5:
                print("Debe ingresar una opción entre 1 y 5.")
                continue
            break
        except ValueError:
            print("Debe ingresar una opción válida (1-5), intenta nuevamente.")
    
    if op == 1:
        agregar_productos(productos)
    elif op == 2:#mostrar_productos(productos)
        mostrar_productos(productos)
    elif op == 3 :#buscar_producto(productos)
        buscar_productos(productos)
    elif op == 4:#producto_mas_caro(productos)
        producto_mas_caro(productos)
    elif op == 5:
        print("Fin del programa")
        break
    



        
              
    


