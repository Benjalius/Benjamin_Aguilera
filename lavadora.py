import time

def lavar_ropa(kilos_necesarios, detergente_necesario, tipo_ropa):
    kgr = int(input(f"¿Cuántos kilos de ropa a poner para {tipo_ropa}?\n"))

    while kgr < kilos_necesarios:
        print(f"No ha alcanzado el mínimo de {kilos_necesarios} kilos.")
        opcion = int(input("¿Qué desea hacer?\n1.-Añadir más ropa\n2.-Terminar\n"))
        if opcion == 1:
            akgr = int(input("¿Cuántos kilos va a agregar?\n"))
            kgr += akgr
        else:
            print("Saliendo del sistema.")
            return

    medd = int(input("¿Cuántas medidas de detergente va a ocupar?\n"))

    while medd < detergente_necesario:
        print(f"Faltan {detergente_necesario - medd} medidas de detergente.")
        amedd = int(input("Añádalas:\n"))
        medd += amedd

    if medd > detergente_necesario:
        print(f"Se ha pasado de la cantidad recomendada ({detergente_necesario}).")
        seguir = input("¿Desea continuar? (si/no)\n").lower()
        while seguir not in ("si", "no"):
            seguir = input("Responda algo válido (si/no):\n").lower()
        if seguir == "no":
            print("No se ha realizado el lavado.\nSaliendo del sistema.")
            return

    print("Lavando la ropa...")
    time.sleep(5)
    print("La ropa está lista.")

def main():
    print("Bienvenido al sistema.\n¿Qué desea hacer?")
    print("1.- Lavar ropa a color.\n2.- Lavar ropa blanca.\n3.- Salir.")
    opc = int(input())

    while opc not in (1, 2, 3):
        print("Escoja una opción válida.")
        opc = int(input())

    if opc == 1:
        print("Usted lavará ropa a color.")
        lavar_ropa(kilos_necesarios=5, detergente_necesario=3, tipo_ropa="ropa a color")
    elif opc == 2:
        print("Usted lavará ropa blanca.")
        lavar_ropa(kilos_necesarios=8, detergente_necesario=4, tipo_ropa="ropa blanca")
    elif opc == 3:
        print("Saliendo del sistema.")

if __name__ == "__main__":
    main()

