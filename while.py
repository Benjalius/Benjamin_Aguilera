#explicaciony uso de while

# num=10

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# import time
# num=10

# while num>0:
#     print(num)
#     time.sleep(2)
#     num-=1

clave=1945
intentos=3
password=int(input("Ingrese la ontraseña :"))

while clave!=password or intentos==0:
    intentos-=1
    print(f"ERROR, le quedan {intentos} intentos")
    password=int(input("Ingrese la contraseña :"))
    if intentos<=1:
        break

if intentos!=0 and clave!=password:
    print("Sistema bloqueado")
else:        
    print("Usted ingresa al sistema")    

#pedir al usuario numeros que se sumen y mostrar al final la suma
#salir si llega a 0

# num=1
# suma=0
# while num!=0:
#     num=int(input("Ingresa un numero: "))
#     suma+=num
# print(f"La suma es {suma}")

# respuesta = int(input("¿cuantas ruedas tiene un auto? "))

# while respuesta!=4:
#    respuesta = int(input("respuesta incorrecta "))

# print("buenisima ")   

