#contraseña

# clave=1945
# intentos=3
# password=int(input("Ingrese la ontraseña :"))

# while clave!=password or intentos==0:
#     intentos-=1
#     print(f"ERROR, le quedan {intentos} intentos")
#     password=int(input("Ingrese la contraseña :"))
#     if intentos<=1:
#         break

# if intentos!=0 and clave!=password:
#     print("Sistema bloqueado")
# else:        
#     print("Usted ingresa al sistema")

# respuesta = int(input("¿cuantas ruedas tiene un auto? "))

# while respuesta!=4:
#    respuesta = int(input("respuesta incorrecta "))

# print("buenisima ")

#calcular el puntaje de credito, debe calcular que tanto credito tiene una persona en cierta entidad financiera
#considerando la siguiente cantidad de ingreso, nivel educacional y nacionalidad
#ingreso: 500k a 1m : 300k / 1m a 1.5m : 650k / 1.500.001 o más : 1m
#nivel educacional : basico x1 /medio x1. / superior x1.5
#nacionalidad : chileno +300k / extranjero +0

# chileno = 300000
# extranjero = 0
# basico = 1
# medio = 1.3
# superior = 1.5
# print("Bienvenido al sistema de credito")
# ingreso = int(input("Ingrese su ingreso mensual: "))
# nivel_educacional = input("Ingrese su nivel educacional (basico, medio, superior): ").lower()
# nacionalidad = input("Ingrese su nacionalidad (chileno, extranjero): ").lower()

# print("Calculando credito...")
# import time
# time.sleep(5)

# if ingreso >= 500000 and ingreso <= 1000000:
#     puntaje_ingreso = 300000
#     if nivel_educacional == "basico":
#         puntaje_ingreso *= 1
#     elif nivel_educacional == "medio":
#         puntaje_ingreso *= 1.3
#     elif nivel_educacional == "superior":
#         puntaje_ingreso *= 1.5
#     else:
#         print("No valido")
#         exit()
# elif ingreso > 1000000 and ingreso <= 1500000:
#     puntaje_ingreso = 650000
#     if nivel_educacional == "basico":
#         puntaje_ingreso *= 1
#     elif nivel_educacional == "medio":
#         puntaje_ingreso *= 1.3
#     elif nivel_educacional == "superior":
#         puntaje_ingreso *= 1.5
#     else:
#         print("No valido")
#         exit()
# elif ingreso > 1500000:
#     puntaje_ingreso = 1000000
#     if nivel_educacional == "basico":
#         puntaje_ingreso *= 1
#     elif nivel_educacional == "medio":
#         puntaje_ingreso *= 1.3
#     elif nivel_educacional == "superior":
#         puntaje_ingreso *= 1.5
#     else:
#         print("No valido")
#         exit()
# else:
#    print("Ingreso no valido")
#    exit()
# print("El ingrso es: ", puntaje_ingreso)
# if nacionalidad == "chileno":
#     puntaje_ingreso += chileno
# elif nivel_educacional == "basico":
#     puntaje_ingreso += chileno
# elif nivel_educacional == "medio":
#     puntaje_ingreso += chileno
# elif nivel_educacional == "superior":
#     puntaje_ingreso += chileno
# else:
#     print("No valido")
#     exit()

# print("Su puntaje de credito es: ", puntaje_ingreso)


#pedir al usuario que ingrese 2 numeros verificando que el segunddo sea mayor
#genera un numero random entre estos 2 e imprima la cantiddad de veces el simbolo (alt+220)

# cantidad = 0
# simbolo = chr(220)

# print("Ingrese 2 numeros")
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero "))
# while num1>=num2:
#     print("El segundo numero debe ser mayor al primero")
#     num1 = int(input("Ingrese el primer numero: "))
#     num2 = int(input("Ingrese el segundo numero "))
#     import random
#     numero_random = random.randint(num1, num2)
#     print("El numero random es: ", numero_random)
#     simbolo = chr(220)
#     cantidad = int(input("Ingrese la cantidad de veces que desea imprimir: "))
#     print(simbolo * cantidad)
#     print("El simbolo se ha impreso ", cantidad, "veces")
# print("El simbolo se ha impreso ", cantidad, "veces")
    
# while cantidad < 1:
#       print("Ingrese una cantidad positiva")
#       cantidad = int(input("Ingrese la cantidad de veces que desea imprimir: ")) 
#       print(simbolo * cantidad)

#V2

# import random

# # Solicitar al usuario los dos números
# num1 = int(input("Ingresa el primer número: "))
# num2 = int(input("Ingresa el segundo número (mayor que el primero): "))

# # Validar que el segundo número sea mayor
# while num2 <= num1:
#     print("Error: el segundo número debe ser mayor que el primero.")
#     num2 = int(input("Ingresa el segundo número nuevamente: "))

# # Generar número aleatorio entre num1 y num2
# aleatorio = random.randint(num1, num2)

# # Imprimir el símbolo ▬ (ALT+220) la cantidad de veces del número aleatorio
# print("Resultado:")
# print("▬" * aleatorio)

#POSIBLES CASOS PARA LA PRUEBA
#Tabla de multiplicar

# num = int(input("Ingrese un numero: "))

# for i in range(1, 11):
#     resultado = num * i
#     print(f"{num} x {i} = {resultado}")

# #Carrito de super

# print("¿Cuántos productos desea agregar?")
# cant = int(input())
# total = 0

# for i in range(cant):
#     print("¿Qué va a llevar? \n a.- Cereal $1000 \n b.- Leche $900 \n c.- Esponja $500 \n d.- Salir")
#     op = input("Elige una opción: ").lower()

#     if op == 'a':
#         print("Usted llevará cereal")
#         total += 1000
#     elif op == 'b':
#         print("Usted llevará leche")
#         total += 900
#     elif op == 'c':
#         print("Usted llevará esponja")
#         total += 500
#     elif op == 'd':
#         print("Usted ha salido")
#         break
#     else:
#         print("Opción inválida, intente de nuevo.")

# print(f"Su total es de ${total}")
# print(f"Más el IVA: ${total * 1.19:.0f}")
# print(f"Total con IVA: ${total * 1.19:.0f}")

#Clave de seguridad

# clave = 1234
# intentos = 3
# password = int(input("Ingrese la contraseña: "))
# while clave != password and intentos > 0:
#     intentos -=1
#     print(f"ERROR, le quedan {intentos} intentos")
#     password = int(input("Ingrese la contraseña: "))
#     if intentos == 0:
#         print("Sistema bloqueado")
#         break
#     elif clave == password:
#         print("Bienvenido al sistema")
    
#pedir al usuario que ingrese 1 numero entero
#si es positivo imprime numero positivo
#si es negativo imprime numero negativo
#si es cero imprime cero
#si no es un numero entero imprime error

# num = int(input("Ingrese un numero entero: "))
# if num > 0:
#     print("El numero es positivo")
# elif num < 0:
#     print("El numero es negativo")
# elif num == 0:
#     print("El numero es cero")
# else:
#     print("Error, numero invalido")

# Ejemplo: Lista de compras organizada por categoría

categorias = ["Frutas", "Verduras", "Lácteos"]
productos = {
    "Frutas": ["Manzanas", "Plátanos", "Frutillas"],
    "Verduras": ["Lechuga", "pepino", "Espinacas"],
    "Lácteos": ["Leche", "Yogur", "Queso"]
}

for categoria in categorias:
    print(f"\nCompras de {categoria}:")
    for producto in productos[categoria]:
        print(f"- {producto}")
