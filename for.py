#pedir al usuario 3 notas y sacar promedio con for

cant = int(input("Ingrese la cantidad de notas: "))
suma = 0

for i in range(cant):
    n1 = float(input("Ingrese la nota: "))
    suma = suma + n1

promedio = suma / cant
print("El promedio es: ", round(promedio))
