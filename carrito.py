#Crear un carrito de super y calcular precio total + iva

productos = {
    'a': {'nombre': 'Cereal', 'precio': 1000},
    'b': {'nombre': 'Leche', 'precio': 900},
    'c': {'nombre': 'Esponja', 'precio': 500}
}

carrito = []

IVA = 0.19

while True:
    print("\n--- Menú de opciones ---")
    print("a. Cereal ($1000)")
    print("b. Leche ($900)")
    print("c. Esponja ($500)")
    print("d. Salir y mostrar total")
    
    opcion = input("Elige una opción: ").lower()

    if opcion in ['a', 'b', 'c']:
        cantidad = int(input(f"¿Cuántos {productos[opcion]['nombre']} deseas? "))
        precio_unitario = productos[opcion]['precio']
        subtotal = precio_unitario * cantidad
        carrito.append(subtotal)
        print(f"Agregaste {cantidad} {productos[opcion]['nombre']}(s) por ${subtotal}")
    elif opcion == 'd':
        total_sin_iva = sum(carrito)
        total_con_iva = total_sin_iva * (1 + IVA)
        print("\n--- Factura final ---")
        print(f"Total sin IVA: ${total_sin_iva:.0f}")
        print(f"IVA (19%): ${total_sin_iva * IVA:.0f}")
        print(f"Total con IVA: ${total_con_iva:.0f}")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
