# Programa para mostrar una tabla de multiplicar elegida por el usuario

# Pedimos al usuario que ingrese un número
numero = int(input("¿De qué número quieres ver la tabla de multiplicar? "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
