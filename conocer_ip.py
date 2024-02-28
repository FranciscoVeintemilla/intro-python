import os
import platform
import socket

while True:
    comando = input('Ingrese el comando a ejecutar: ')
    if comando.lower() == 'ip':
        # Obtiene el nombre del host y la dirección IP
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print('Dirección IP: ', ip_address)
    elif comando.lower() == 'sistema operativo':
        # Imprime el tipo de sistema operativo
        print('Sistema Operativo: ', platform.system(), platform.release())
    else:
        print('Comando no reconocido')
