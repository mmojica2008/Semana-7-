matriz = []
filas = 0
columnas = 0

def pedirTamaño():
    global filas, columnas
    filas = int(input("Tamaño de filas: "))
    columnas = int(input("Tamaño de columnas: "))


def leerValor(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero")

def agregarElemento():
    for i in range (filas):
        matriz.append([])
        for j in range (columnas):
            dato = leerValor(f"Valor [{i}, {j}]: ")
            matriz[i].append(int(input(f"valor ({i}, {j}")))

pedirTamaño(2, 2)
print(filas, columnas)
agregarElemento()

def menu():
    print("""
1. Asignar tamaño
2. Agregar elementos
3. Salir
""")
    op = leerValor()
    return op

def main():
    while True:
     op = menu()
     if op == 1:
         pedirTamaño()
     elif op == 2:
         agregarElemento()
     elif op == 3:
         print("Adios")
         break

main()             