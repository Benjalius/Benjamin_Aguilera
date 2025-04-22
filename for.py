#pedir al usuario 3 notas y sacar promedio con for

# cant = int(input("Ingrese la cantidad de notas: "))
# suma = 0

# for i in range(cant):
#     n1 = float(input("Ingrese la nota: "))
#     suma = suma + n1

# promedio = suma / cant
# print("El promedio es: ", round(promedio))

# designar 2 cantidades. preguntar la cantidad de votantes
# por cada votante debe preguntar por quien votará
# contar votos y mostrar resultados
# definir ganador



#cantidad de notas y promediarlas

print("Ingresar cantidad de notas")
suma = 0
cantN=int(input())
for i in range(cantN):
    print("Ingrese la nota ",i +1)
    nota=float(input())
    # suma+=nota
    suma=suma+nota

prom=suma/cantN
print("Su promedio es ", prom)

if prom >=4:
     print("El alumno aprueba")
else:
     print("El alumno reprueba")    