
producto = {
    "Mouse":[10,15000],
    "Teclado" : [5,25000],
    "Monitor" : [3,180000]
}

def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    
    if nombre in productos:
        print("El producto ya existe!")
        return

    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese precio $: "))

    productos[nombre] = [stock,precio]
    print("Producto agregado correctamente!")


productos = {} #diccionario vacío

while True:
    print("----  MENU ----")
    print("1. Agregar Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            op = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("Debe ingresar un opción válida (1-5), intente nuevamente")

    if op == 1 :
        agregar_producto(productos)
        
    elif op == 2:
        #mostrar_productos(productos)
        print(productos)
    elif op == 3 :
        #buscar_producto(productos)
        print("buscar")
    elif op == 4:
        #producto_mas_caro(productos)
        print("más caro")
    elif op == 5:
        print("Fin del programa")
        break
    else:
        print("Opción no válida")