# print("Ingrese 3 numeros para sacar el promedio")
# n1 = int(input("Ingrese el primer numero"))
# n2 = int(input("Ingrese el segundo numero"))
# n3 = int(input("Ingrese el tercer numero"))
# prom = (n1 + n1 + n3)/3
# print("El promedio es", prom)

# if prom >=40:
#     print("El alumno aprueba")
# else:
#     print("El alumno reprueba")    

# edad = int(input("Ingrese su edad"))

# if edad>=18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

# edad = int(input("Ingrese su edad"))
# if edad < 12:
#     print("Eres un niño")
# elif edad >= 12 and edad <= 17:
#     print("Eres un adolecente")
# else:
#     print("Eres un adulto")

#ingrese 3 numeros y muestre el mayor de ellos

n1 = int(input("Ingrese el primer numero"))
n2 = int(input("Ingrese el segundo numero"))
n3 = int(input("Ingrese el tercer numero"))

if n1>n2 and n1>n3:
    print(" El numero ", n1, "es el mayor")
elif n2>n3:
    print(" El numero ", n2, "es el mayor")
else:
    print(" El numero ", n3, "es el mayor ")