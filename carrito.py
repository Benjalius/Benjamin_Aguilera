#Crear un carrito de super y calcular precio total + iva

# productos = {
#     'a': {'nombre': 'Cereal', 'precio': 1000},
#     'b': {'nombre': 'Leche', 'precio': 900},
#     'c': {'nombre': 'Esponja', 'precio': 500}
# }

# carrito = []

# IVA = 0.19

# while True:
#     print("\n--- Menú de opciones ---")
#     print("a. Cereal ($1000)")
#     print("b. Leche ($900)")
#     print("c. Esponja ($500)")
#     print("d. Salir y mostrar total")
    
#     opcion = input("Elige una opción: ").lower()

#     if opcion in ['a', 'b', 'c']:
#         cantidad = int(input(f"¿Cuántos {productos[opcion]['nombre']} deseas? "))
#         precio_unitario = productos[opcion]['precio']
#         subtotal = precio_unitario * cantidad
#         carrito.append(subtotal)
#         print(f"Agregaste {cantidad} {productos[opcion]['nombre']}(s) por ${subtotal}")
#     elif opcion == 'd':
#         total_sin_iva = sum(carrito)
#         total_con_iva = total_sin_iva * (1 + IVA)
#         print("\n--- Factura final ---")
#         print(f"Total sin IVA: ${total_sin_iva:.0f}")
#         print(f"IVA (19%): ${total_sin_iva * IVA:.0f}")
#         print(f"Total con IVA: ${total_con_iva:.0f}")
#         break
#     else:
#         print("Opción inválida. Intenta de nuevo.")

#version 2
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
# print(f"Más el IVA: ${total * 0.19:.0f}")
# print(f"Total con IVA: ${total * 1.19:.0f}")


