# Importar el módulo ipaddress
import ipaddress

# Definir las redes de clase A, B y C
classA = ipaddress.IPv4Network("10.0.0.0/8")
classB = ipaddress.IPv4Network("172.16.0.0/12")
classC = ipaddress.IPv4Network("192.168.0.0/16")

# Pedir al usuario que introduzca una dirección IP v4 válida
ip = input("Introduce una dirección IP v4: ")

# Crear un objeto IPv4Address con la dirección IP introducida
ip = ipaddress.IPv4Address(ip)

# Comprobar a qué clase pertenece la dirección IP
if ip in classA:
    print("La dirección IP pertenece a la clase A")
elif ip in classB:
    print("La dirección IP pertenece a la clase B")
elif ip in classC:
    print("La dirección IP pertenece a la clase C")
else:
    print("La dirección IP no pertenece a ninguna de las clases A, B o C")
