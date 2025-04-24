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

# c1="coyote"
# c2="porky"
# cantvotos1=0
# cantvotos2=0

# cantV=int(input("Ingrese la canidad de votantes: "))

# for i in range(cantV):
#     print("por quien votará?: 1.-{c1}, 2.-{c2}")
#     voto=input()

#     if voto=="1":
#         print(f"Usted votó por {c1}")
#         cantvotos1+=1
#     else:
#         print(f"Ustedd votó por {c2}")
#         cantvotos2+=1

# print(f"la cantidad de votos de {c1} es {cantvotos1}")
# print(f"la cantidad de votos de {c2} es {cantvotos2}")

# if cantvotos1>cantvotos2:
#     print(f"ganó {c1}")
# elif cantvotos2>cantvotos1:
#     print(f"ganó {c2}")
    
# cantidad de notas y promediarlas

# print("Ingresar cantidad de notas")
# suma = 0
# notas_azule = 0
# cantN=int(input())
# for i in range(cantN):
#     print("Ingrese la nota ",i +1)
#     nota=float(input())
#     if nota >=4:
#          notas_azules +=1
#     # suma+=nota
#     suma=suma+nota

# prom=suma/cantN
# print("Su promedio es ", round (prom, 1))
# print("La cantidad de notas aprobadas es ", notas_azules)

# if prom >=4:
#      print("El alumno aprueba")
# else:
#      print("El alumno reprueba")    

#pedir al usuario una frae y cuente los caracteres

# frase = input("Ingrese un nombre")
# cont = 0
# for i in frase:
#     cont +=1
# print(f"La cantidadd de caracteres es {cont}")

frase=input(" ingrese su frase ")
cantcar=0
v=0
cons=0
e=0
for i in frase:
    print(i)
    cantcar+=1
    if i.lower() in "aeiouAEIOU":
        v+=1
        #v=v+1 
    elif i==" ":
        e+=1
    else:
        cons+=1

print(f"El total de caracteres es {cantcar}")
print(f"El total de vocales  es {v}")
print(f"El total de consonantes  es {cons}")



