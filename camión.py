#cargar camion con limite de 50 cajas
#preguntar cuantas cajas se cargan
#si aún hay espacio, dejar cargar cajas
#si sobrepasa el limite, poner camion lleno sobran _ cajas

limite = 50
cajas_cargadas = 0
cajas_sobrantes = 0

print("Carga de camión (capacidad: 50 cajas)")

while cajas_cargadas < limite:
    cajas = int(input("¿Cuántas cajas deseas cargar? "))

    if cajas_cargadas + cajas <= limite:
        cajas_cargadas += cajas
        print("Cajas cargadas hasta ahora:", cajas_cargadas)
    else:
        cajas_sobrantes = (cajas_cargadas + cajas) - limite
        cajas_cargadas = limite
        print("Camión lleno. Sobran", cajas_sobrantes, "cajas.")

print("Carga finalizada.")

