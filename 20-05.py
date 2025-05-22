#perros de caza
#pedir al usuario la cantidad de perros
#mostrar cuota minima de conejos
#mostrar resumen de perro que cumplieron y los que no

# import random, time

# perros=int(input("Ingresar cantidad de perros que van a la caza"))
# cuota=3
# cumple=0
# print("comienza la caza")
# for p in range(perros):
#     conejos=random.randint(0,6)
#     if conejos>=cuota:
#         print(f"El perro {p+1} trajo {conejos} conejos")
#         print("Hay flete")
#         cumple+=1
#     else:
#         print(f"El perro {p+1} trajo {conejos} conejos")
#         print("No hay flete")


#quiere pasar el ramo?
#preguntar cantidad de rojos en el curso
#los talleres en el semestre son 4
#por cada taller asistido son 0.3 decimas
#si el alumno tiene mas de 1 punto tiene la bendicion del profe
#si no, nada que hacer

# talleres_asistidos = int(input("¿Cuántos talleres asistió el alumno? (de 0 a 4): "))


# if talleres_asistidos < 0 or talleres_asistidos > 4:
#     print("Cantidad inválida de talleres.")
# else:
#     puntaje_total = talleres_asistidos * 0.3  
#     print(f"Puntaje acumulado: {puntaje_total:.2f}")

#     if puntaje_total > 1.0:
#         print("El alumno tiene la bendición del profe. ¡Aprueba!")
#     else:
#         print("Nada que hacer... El alumno reprueba.")

#     nota_final = 4.0 + puntaje_total
#     print(f"La nota final del alumno: {nota_final:.2f}")


#crear menu para lavar autos 1.-cursar pago del lavado 2.-ver ventas diarias 3.-salir
#lavado con 3 niveles
#full $15.000, standar $10.000, basico $7.000
#al mostar ventas diarias, debe mostrar la cantidad de autos ingresados y monto total
#mostrar monto mas alto pagado