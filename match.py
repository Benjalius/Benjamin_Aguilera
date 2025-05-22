#uso y explicacion del match
#calculadora 

# def suma():
#     n1 = int(input("Ingrese un número: "))
#     n2 = int(input("Ingrese otro número: "))
#     print("El resultado es", n1 + n2)

# def resta():
#     n1 = int(input("Ingrese un número: "))
#     n2 = int(input("Ingrese otro número: "))
#     print("El resultado es", n1 - n2)

# def multi():
#     n1 = int(input("Ingrese un número: "))
#     n2 = int(input("Ingrese otro número: "))
#     print("El resultado es", n1 * n2)

# def divi():
#     n1 = int(input("Ingrese un número: "))
#     n2 = int(input("Ingrese otro número: "))
#     if n2 != 0:
#         print("El resultado es", n1 / n2)
#     else:
#         print("Error: no se puede dividir por cero.")

# def calcu():
#     while True:
#         op = int(input('''Seleccione una opción:
# 1.- Suma
# 2.- Resta
# 3.- Multiplicación
# 4.- División
# 5.- Salir
# > '''))

#         match op:
#             case 1:
#                 suma()
#             case 2:
#                 resta()
#             case 3:
#                 multi()
#             case 4:
#                 divi()
#             case 5:
#                 print("Salir")
#                 break
#             case _:
#                 print("Opción inválida")

# calcu()

#crear menu de carrito con las siguientes opciones
# 1.- ingresar nombre del usuario y este será mostrado en la boleta con un lasudo
# 2.- comprar, poner productos para poder comprar con su precio correspondiente
# 3.- sacar la boleta, calcular precio neto y precio más IVA. mostrar total
# 4.- salir
# 5.- almenos 3 productos
# 6.- sin limite de compra
# 7.- se puede salir en cualquier momento
# Recomencacion usar match

# total=0
# carrito=0
# while True:
#     print('''Seleccione una opcion
#         1.-Ingresar Nombre
#         2.-Comprar
#         3.-Mostrar boleta
#         4.-Salir
#         ''')

#     op=int(input())

#     match op:
#         case 1:
#             nombre=input("ingres su nombre: ")
#         case 2:
#             while True:
#                 print('''
#                 1.- Manzana $1200
#                 2.- Pera $1400
#                 3.- Platano $1000
#                 4.- Volver al menu principal
#                 ''')
#                 opc=int(input())
#                 match opc:
#                     case 1:
#                        total+=1200
#                     case 2:
#                        total+=1400
#                     case 3:
#                        total+=1000
#                     case 4:
#                         break
#                     case _:
#                         print("Producto no valido")
#                 print("Su total parcial es ", total)
#                 carrito+=1        
#         case 3:
#             print(f'''
#                 ----------------0-----------------  
#                 EL TOTAL DE ARTICULOS ES {carrito}
#                 Su total neto es {total}
#                 Su total mas IVA es {total*1.19}
#                 Gracias {nombre} por venir
#                 Vuelva Pronto
#                 ----------------0-----------------  
#                   ''')
#         case 4:
#             break
#         case _:
#             print("opcion invalida")

#promedios por cantidad de alumnos
#pedir cantidad de alumnos
#pedir notas por alumno
#promediar a cada alumno
#mostara si el alumno aprueba o repueba
#BONUS: mostar el promedio de todos los alumnos ingresados

'''Ingrese cant de alumnos: 5
Ingrese cantidad de notas del alumno 1 :3 
Ingrese la nota 1 del alumno 1
Ingrese la nota 2 del alumno 1
Ingrese la nota 3 del alumno 1
El promedio del alumno 1 es : 5.6
El alumno 1 Aprobó
Ingrese la nota 1 del alumno 2
...
...
...
El promedio general del curso es: 
'''

# cant_alumn=int(input("Ingrese la cantidad de alumnos: "))

# prom_general=0
# cont_prom_gen=0

# for j in range (cant_alumn):
#     cant_not=int(input(f"Ingrese su cantidad de notas del alumno {j+1} : "))
#     notas=0
#     for i in range (cant_not):
#         nota=float(input(f"Ingrese la nota n° {i+1} del alumno {j+1}: "))
#         notas+=nota
#     Prom=notas/cant_not
#     print(f"El promedio del alumno {j+1} es {Prom}")
#     if Prom>=4:
#         print(f"El alumno {j+1} ha aprobado")
#     else:
#         print(f"El alumno {j+1} ha reprobado")
#     cont_prom_gen+=Prom

# prom_general=cont_prom_gen/cant_alumn
# print(f"El promedio general del curso es {prom_general}")

#creacion de armas en minecraft
#crear espadas de diamante
#para crear espada de diamante necesitas 2 diamantes y 1 palo
#para obtener los recursos debes tener el siguiente menu
#1.- minar, se buscan recursos.la posibilidad de encontrar diamante es 1 entre 7 y 1 palo entre 3 y carbon 1 entre 3
#minar toma 3 segundos
#2.-consultar recursos, muestra los recursos acumulados
#3.-crear espadas, va a crear tantas espadas posibles como se pueda
#4.-salir

import time, random

madera = 0
hierro = 0
diamante = 0
carbon = 0
palos = 0

while True:
    print('''
1.- Talar
2.- Minar
3.- Consultar inventario
4.- Craftear
5.- Salir
''')

    op = int(input("Ingrese una opción: "))

    if op == 1:
        print("Talaste madera")
        madera += 1
        palos += 2
        time.sleep(2)

    elif op == 2:
        print("Minaste")
        time.sleep(2)

        if random.randint(1, 7) == 1:
            print("Encontraste un diamante")
            diamante += 1
        if random.randint(1, 3) == 1:
            print("Encontraste un palo")
            palos += 1
        if random.randint(1, 3) == 1:
            print("Encontraste carbón")
            carbon += 1
        time.sleep(2)

    elif op == 3:
        print(f'''
Madera: {madera}
Hierro: {hierro}
Diamante: {diamante}
Carbon: {carbon}
Palos: {palos}
''')
        time.sleep(2)

    elif op == 4:
        espadas = min(diamante // 2, palos // 1)
        if espadas > 0:
            print(f"Creaste {espadas} espadas de diamante")
            diamante -= espadas * 2
            palos -= espadas * 1
        else:
            print("No tienes los recursos suficientes para crear espadas")
        time.sleep(2)

    elif op == 5:
        print("Saliendo del juego...")
        break

    else:
        print("Opción inválida")
        time.sleep(2)

#NIGGA