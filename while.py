#explicaciony uso de while

# num=10

# while num<5:
#     print("hola")
#     num+=1

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